""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class ReceiptPerPhoneSchema(schema.ResponseSchema):
    """ReceiptPerPhone - 每个目的手机号的发送回执信息"""

    fields = {
        "CostCount": fields.Int(required=True, load_from="CostCount"),
        "Phone": fields.Str(required=True, load_from="Phone"),
        "ReceiptCode": fields.Str(required=True, load_from="ReceiptCode"),
        "ReceiptDesc": fields.Str(required=True, load_from="ReceiptDesc"),
        "ReceiptResult": fields.Str(required=True, load_from="ReceiptResult"),
        "ReceiptTime": fields.Int(required=True, load_from="ReceiptTime"),
        "UserId": fields.Str(required=True, load_from="UserId"),
    }


class ReceiptPerSessionSchema(schema.ResponseSchema):
    """ReceiptPerSession - 每个提交的回执结果集合"""

    fields = {
        "ReceiptSet": fields.List(ReceiptPerPhoneSchema()),
        "SessionNo": fields.Str(required=True, load_from="SessionNo"),
    }


class OutSignatureSchema(schema.ResponseSchema):
    """OutSignature - 短信签名"""

    fields = {
        "ErrDesc": fields.Str(required=True, load_from="ErrDesc"),
        "SigContent": fields.Str(required=True, load_from="SigContent"),
        "SigId": fields.Str(required=True, load_from="SigId"),
        "Status": fields.Int(required=True, load_from="Status"),
    }


class OutTemplateSchema(schema.ResponseSchema):
    """OutTemplate - 短信模板"""

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "ErrDesc": fields.Str(required=True, load_from="ErrDesc"),
        "Instruction": fields.Str(required=False, load_from="Instruction"),
        "Purpose": fields.Int(required=True, load_from="Purpose"),
        "Remark": fields.Str(required=True, load_from="Remark"),
        "Status": fields.Int(required=True, load_from="Status"),
        "Template": fields.Str(required=True, load_from="Template"),
        "TemplateId": fields.Str(required=True, load_from="TemplateId"),
        "TemplateName": fields.Str(required=True, load_from="TemplateName"),
        "UnsubscribeInfo": fields.Str(
            required=True, load_from="UnsubscribeInfo"
        ),
    }


class FailPhoneDetailSchema(schema.ResponseSchema):
    """FailPhoneDetail - 批量任务中，未能成功发送的号码及其原因"""

    fields = {
        "ExtendCode": fields.Str(required=False, load_from="ExtendCode"),
        "FailureDetails": fields.Str(
            required=False, load_from="FailureDetails"
        ),
        "Phone": fields.Str(required=True, load_from="Phone"),
        "TemplateParams": fields.List(fields.Str()),
        "UserId": fields.Str(required=False, load_from="UserId"),
    }


class BatchInfoSchema(schema.ResponseSchema):
    """BatchInfo - 批量发送任务中未能成功发送的信息详情，“模板+签名”粒度"""

    fields = {
        "FailureDetails": fields.Str(
            required=False, load_from="FailureDetails"
        ),
        "SigContent": fields.Str(required=True, load_from="SigContent"),
        "Target": fields.List(FailPhoneDetailSchema()),
        "TemplateId": fields.Str(required=True, load_from="TemplateId"),
    }
