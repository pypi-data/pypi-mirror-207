# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SqlQueryArgs', 'SqlQuery']

@pulumi.input_type
class SqlQueryArgs:
    def __init__(__self__, *,
                 data_source_id: pulumi.Input[str],
                 query: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['SqlQueryParameterArgs']]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 run_as_role: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input['SqlQueryScheduleArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SqlQuery resource.
        """
        pulumi.set(__self__, "data_source_id", data_source_id)
        pulumi.set(__self__, "query", query)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if run_as_role is not None:
            pulumi.set(__self__, "run_as_role", run_as_role)
        if schedule is not None:
            warnings.warn("""Operations on `databricks_sql_query` schedules are deprecated. Please use `databricks_job` resource to schedule a `sql_task`.""", DeprecationWarning)
            pulumi.log.warn("""schedule is deprecated: Operations on `databricks_sql_query` schedules are deprecated. Please use `databricks_job` resource to schedule a `sql_task`.""")
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "data_source_id")

    @data_source_id.setter
    def data_source_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_source_id", value)

    @property
    @pulumi.getter
    def query(self) -> pulumi.Input[str]:
        return pulumi.get(self, "query")

    @query.setter
    def query(self, value: pulumi.Input[str]):
        pulumi.set(self, "query", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SqlQueryParameterArgs']]]]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SqlQueryParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter(name="runAsRole")
    def run_as_role(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "run_as_role")

    @run_as_role.setter
    def run_as_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_as_role", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['SqlQueryScheduleArgs']]:
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['SqlQueryScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _SqlQueryState:
    def __init__(__self__, *,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['SqlQueryParameterArgs']]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 run_as_role: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input['SqlQueryScheduleArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering SqlQuery resources.
        """
        if data_source_id is not None:
            pulumi.set(__self__, "data_source_id", data_source_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if query is not None:
            pulumi.set(__self__, "query", query)
        if run_as_role is not None:
            pulumi.set(__self__, "run_as_role", run_as_role)
        if schedule is not None:
            warnings.warn("""Operations on `databricks_sql_query` schedules are deprecated. Please use `databricks_job` resource to schedule a `sql_task`.""", DeprecationWarning)
            pulumi.log.warn("""schedule is deprecated: Operations on `databricks_sql_query` schedules are deprecated. Please use `databricks_job` resource to schedule a `sql_task`.""")
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "data_source_id")

    @data_source_id.setter
    def data_source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_source_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SqlQueryParameterArgs']]]]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SqlQueryParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "query")

    @query.setter
    def query(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query", value)

    @property
    @pulumi.getter(name="runAsRole")
    def run_as_role(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "run_as_role")

    @run_as_role.setter
    def run_as_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_as_role", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['SqlQueryScheduleArgs']]:
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['SqlQueryScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class SqlQuery(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SqlQueryParameterArgs']]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 run_as_role: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['SqlQueryScheduleArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Import

        You can import a `databricks_sql_query` resource with ID like the followingbash

        ```sh
         $ pulumi import databricks:index/sqlQuery:SqlQuery this <query-id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlQueryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        You can import a `databricks_sql_query` resource with ID like the followingbash

        ```sh
         $ pulumi import databricks:index/sqlQuery:SqlQuery this <query-id>
        ```

        :param str resource_name: The name of the resource.
        :param SqlQueryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlQueryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SqlQueryParameterArgs']]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 run_as_role: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['SqlQueryScheduleArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlQueryArgs.__new__(SqlQueryArgs)

            if data_source_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_source_id'")
            __props__.__dict__["data_source_id"] = data_source_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["parent"] = parent
            if query is None and not opts.urn:
                raise TypeError("Missing required property 'query'")
            __props__.__dict__["query"] = query
            __props__.__dict__["run_as_role"] = run_as_role
            if schedule is not None and not opts.urn:
                warnings.warn("""Operations on `databricks_sql_query` schedules are deprecated. Please use `databricks_job` resource to schedule a `sql_task`.""", DeprecationWarning)
                pulumi.log.warn("""schedule is deprecated: Operations on `databricks_sql_query` schedules are deprecated. Please use `databricks_job` resource to schedule a `sql_task`.""")
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["tags"] = tags
        super(SqlQuery, __self__).__init__(
            'databricks:index/sqlQuery:SqlQuery',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            data_source_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SqlQueryParameterArgs']]]]] = None,
            parent: Optional[pulumi.Input[str]] = None,
            query: Optional[pulumi.Input[str]] = None,
            run_as_role: Optional[pulumi.Input[str]] = None,
            schedule: Optional[pulumi.Input[pulumi.InputType['SqlQueryScheduleArgs']]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'SqlQuery':
        """
        Get an existing SqlQuery resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SqlQueryState.__new__(_SqlQueryState)

        __props__.__dict__["data_source_id"] = data_source_id
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["parent"] = parent
        __props__.__dict__["query"] = query
        __props__.__dict__["run_as_role"] = run_as_role
        __props__.__dict__["schedule"] = schedule
        __props__.__dict__["tags"] = tags
        return SqlQuery(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data_source_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence['outputs.SqlQueryParameter']]]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def query(self) -> pulumi.Output[str]:
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="runAsRole")
    def run_as_role(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "run_as_role")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.SqlQuerySchedule']]:
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tags")

