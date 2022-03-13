from applications.models import db
from applications.models.admin_measure_data import (
    MeasureData, MeasureDataSchema)
from applications.models.admin_photo import (
    Photo, PhotoSchema, DetectionData, DetectionDataSchema)
from applications.service.common.curd import model_to_dicts


def get_measure_data(page, limit):
    measure_data_all = MeasureData.query.paginate(page=page,
                                                  per_page=limit,
                                                  error_out=False)

    count = MeasureData.query.count()
    data = model_to_dicts(Schema=MeasureDataSchema,
                          model=measure_data_all.items)
    return data, count


def save_measure_data(req_json):
    coord_xyz = req_json.get('coordXyz')
    measure_address = req_json.get('measureAddress')
    measure_status = req_json.get('measureStatus')
    measure_info = req_json.get('measureInfo')

    d = MeasureData(coord_xyz=coord_xyz,
                    measure_address=measure_address,
                    measure_status=measure_status,
                    measure_info=measure_info)
    db.session.add(d)
    db.session.commit()
    return d.id


def bulk_save_measure_data(req_json):
    datas = req_json.get('data')
    db.session.bulk_insert_mappings(MeasureData, datas)
    db.session.commit()
    return True


def update_measure_data(req_json):
    id = req_json.get('dataId')
    MeasureData.query.filter_by(id=id).update({
        "coord_xyz": req_json.get('coordXyz'),
        "measure_address": req_json.get('measureAddress'),
        "measure_status": req_json.get('measureStatus'),
        "measure_info": req_json.get('measureInfo')
    })
    db.session.commit()
    return


def delete_data_by_id(id):
    res = MeasureData.query.filter_by(id=id).delete()
    db.session.commit()
    return res
