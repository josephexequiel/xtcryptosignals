__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    Schema,
    fields,
)
from xtcryptosignals.server.api.common.schemas import OutputSchema


class NotificationRuleAddInputSchema(Schema):
    coin_token = fields.String(required=True)
    metric = fields.String(required=True)
    interval = fields.String(required=True)
    percentage = fields.Float(required=True)


class NotificationOutputSchema(OutputSchema):
    txt = fields.String(required=True)
    created_on = fields.DateTime(required=True, format="%Y-%m-%d %H:%M:%S")


class NotificationRulesOutputSchema(OutputSchema):
    coin_token = fields.String(required=True)
    metric = fields.String(required=True)
    interval = fields.String(required=True)
    percentage = fields.Float(required=True)
    created_on = fields.DateTime(required=True, format="%Y-%m-%d %H:%M:%S")