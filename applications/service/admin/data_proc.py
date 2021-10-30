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

