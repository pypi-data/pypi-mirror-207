""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.cube.schemas import apis


class CubeClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(CubeClient, self).__init__(config, transport, middleware, logger)

    def create_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateCubeDeployment -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **Deployment** (str) - (Required)
        - **SubnetId** (str) - (Required)
        - **VPCId** (str) - (Required)
        - **Zone** (str) - (Required)
        - **ChargeType** (str) -
        - **CpuPlatform** (str) -
        - **KubeConfig** (str) -
        - **Name** (str) -
        - **Quantity** (int) -
        - **Tag** (str) -

        **Response**

        - **Deployment** (str) -
        - **DeploymentId** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateCubeDeploymentRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateCubeDeployment", d, **kwargs)
        return apis.CreateCubeDeploymentResponseSchema().loads(resp)

    def create_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateCubePod -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **Pod** (str) - (Required)
        - **SubnetId** (str) - (Required)
        - **VPCId** (str) - (Required)
        - **Zone** (str) - (Required)
        - **ChargeType** (str) -
        - **CouponId** (str) -
        - **CpuPlatform** (str) -
        - **Group** (str) -
        - **KubeConfig** (str) -
        - **Name** (str) -
        - **Quantity** (int) -
        - **Tag** (str) -

        **Response**

        - **CubeId** (str) -
        - **Pod** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.CreateCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateCubePod", d, **kwargs)
        return apis.CreateCubePodResponseSchema().loads(resp)

    def delete_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteCubeDeployment -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **DeploymentId** (str) - (Required)
        - **Zone** (str) -

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteCubeDeploymentRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("DeleteCubeDeployment", d, **kwargs)
        return apis.DeleteCubeDeploymentResponseSchema().loads(resp)

    def delete_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteCubePod -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **CubeId** (str) -
        - **ReleaseEIP** (bool) -
        - **Uid** (str) -
        - **Zone** (str) -

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.DeleteCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("DeleteCubePod", d, **kwargs)
        return apis.DeleteCubePodResponseSchema().loads(resp)

    def get_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeDeployment -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **DeploymentId** (str) - (Required)
        - **Zone** (str) -

        **Response**

        - **Deployment** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeDeploymentRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("GetCubeDeployment", d, **kwargs)
        return apis.GetCubeDeploymentResponseSchema().loads(resp)

    def get_cube_exec_token(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeExecToken -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **ContainerName** (str) - (Required)
        - **CubeId** (str) -
        - **Uid** (str) -
        - **Zone** (str) -

        **Response**

        - **TerminalUrl** (str) -
        - **Token** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeExecTokenRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("GetCubeExecToken", d, **kwargs)
        return apis.GetCubeExecTokenResponseSchema().loads(resp)

    def get_cube_extend_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeExtendInfo -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **CubeIds** (str) - (Required)
        - **Zone** (str) -

        **Response**

        - **ExtendInfo** (list) - 见 **CubeExtendInfo** 模型定义

        **Response Model**

        **CubeExtendInfo**
        - **CubeId** (str) -
        - **Eip** (list) - 见 **EIPSet** 模型定义
        - **Expiration** (int) -
        - **Name** (str) -
        - **Tag** (str) -


        **EIPSet**
        - **Bandwidth** (int) -
        - **BandwidthType** (int) -
        - **CreateTime** (int) -
        - **EIPAddr** (list) - 见 **EIPAddr** 模型定义
        - **EIPId** (str) -
        - **PayMode** (str) -
        - **Resource** (str) -
        - **Status** (str) -
        - **Weight** (int) -


        **EIPAddr**
        - **IP** (str) -
        - **OperatorName** (str) -


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeExtendInfoRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("GetCubeExtendInfo", d, **kwargs)
        return apis.GetCubeExtendInfoResponseSchema().loads(resp)

    def get_cube_metrics(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeMetrics -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **BeginTime** (int) - (Required)
        - **ContainerName** (str) - (Required)
        - **EndTime** (int) - (Required)
        - **ResourceId** (str) - (Required)
        - **Zone** (str) - (Required)
        - **MetricName** (list) -

        **Response**

        - **DataSets** (list) - 见 **MetricDataSet** 模型定义
        - **Message** (str) -

        **Response Model**

        **MetricDataSet**
        - **MetricName** (str) -
        - **Values** (list) - 见 **ValueSet** 模型定义


        **ValueSet**
        - **Timestamp** (int) -
        - **Value** (float) -


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeMetricsRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("GetCubeMetrics", d, **kwargs)
        return apis.GetCubeMetricsResponseSchema().loads(resp)

    def get_cube_pod(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """GetCubePod -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **CubeId** (str) -
        - **Uid** (str) -
        - **Zone** (str) -

        **Response**

        - **Pod** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("GetCubePod", d, **kwargs)
        return apis.GetCubePodResponseSchema().loads(resp)

    def get_cube_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubePrice -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **ChargeType** (str) - (Required)
        - **Count** (str) - (Required)
        - **Cpu** (str) - (Required)
        - **Mem** (str) - (Required)
        - **Quantity** (int) - (Required)
        - **Zone** (str) - (Required)

        **Response**

        - **OriginalPrice** (int) -
        - **Price** (int) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubePriceRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("GetCubePrice", d, **kwargs)
        return apis.GetCubePriceResponseSchema().loads(resp)

    def get_cube_token(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetCubeToken -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **ContainerName** (str) - (Required)
        - **CubeId** (str) -
        - **Uid** (str) -
        - **Zone** (str) -

        **Response**

        - **Token** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.GetCubeTokenRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("GetCubeToken", d, **kwargs)
        return apis.GetCubeTokenResponseSchema().loads(resp)

    def list_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListCubeDeployment -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **Limit** (int) - (Required)
        - **Offset** (int) - (Required)
        - **Zone** (str) -

        **Response**

        - **Deployments** (list) -
        - **TotalCount** (int) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListCubeDeploymentRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("ListCubeDeployment", d, **kwargs)
        return apis.ListCubeDeploymentResponseSchema().loads(resp)

    def list_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListCubePod -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **DeploymentId** (str) -
        - **Group** (str) -
        - **Limit** (int) -
        - **Offset** (int) -
        - **SubnetId** (str) -
        - **VPCId** (str) -
        - **Zone** (str) -

        **Response**

        - **Pods** (list) -
        - **TotalCount** (int) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ListCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("ListCubePod", d, **kwargs)
        return apis.ListCubePodResponseSchema().loads(resp)

    def modify_cube_extend_info(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyCubeExtendInfo -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **CubeId** (str) - (Required)
        - **Name** (str) -
        - **Zone** (str) -

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyCubeExtendInfoRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("ModifyCubeExtendInfo", d, **kwargs)
        return apis.ModifyCubeExtendInfoResponseSchema().loads(resp)

    def modify_cube_tag(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ModifyCubeTag -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **CubeId** (str) - (Required)
        - **Tag** (str) - (Required)
        - **Zone** (str) -

        **Response**

        - **CubeId** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.ModifyCubeTagRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("ModifyCubeTag", d, **kwargs)
        return apis.ModifyCubeTagResponseSchema().loads(resp)

    def reboot_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RebootCubePod -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **CubeId** (str) - (Required)
        - **Zone** (str) -

        **Response**


        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RebootCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("RebootCubePod", d, **kwargs)
        return apis.RebootCubePodResponseSchema().loads(resp)

    def renew_cube_pod(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """RenewCubePod -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **CubeId** (str) - (Required)
        - **Pod** (str) - (Required)
        - **Zone** (str) -

        **Response**

        - **Pod** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.RenewCubePodRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("RenewCubePod", d, **kwargs)
        return apis.RenewCubePodResponseSchema().loads(resp)

    def update_cube_deployment(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateCubeDeployment -

        **Request**

        - **ProjectId** (str) - (Config)
        - **Region** (str) - (Config)
        - **Deployment** (str) - (Required)
        - **DeploymentId** (str) - (Required)
        - **Name** (str) -
        - **Zone** (str) -

        **Response**

        - **Deployment** (str) -

        """
        # build request
        d = {
            "ProjectId": self.config.project_id,
            "Region": self.config.region,
        }
        req and d.update(req)
        d = apis.UpdateCubeDeploymentRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("UpdateCubeDeployment", d, **kwargs)
        return apis.UpdateCubeDeploymentResponseSchema().loads(resp)
