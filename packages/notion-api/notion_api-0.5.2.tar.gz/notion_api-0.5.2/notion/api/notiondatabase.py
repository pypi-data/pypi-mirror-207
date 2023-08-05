# MIT License

# Copyright (c) 2023 ayvi-0001

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from functools import cached_property
from types import ModuleType
from typing import TYPE_CHECKING, Any, MutableMapping, Optional, Sequence, Union, cast

try:
    import orjson

    default_json: ModuleType = orjson
except ModuleNotFoundError:
    import json

    default_json: ModuleType = json

from notion.api.blockmixin import _TokenBlockMixin
from notion.api.client import _NLOG
from notion.api.notionblock import Block
from notion.exceptions.errors import NotionValidationError
from notion.properties.build import NotionObject, build_payload
from notion.properties.common import Parent
from notion.properties.files import Cover, Icon
from notion.properties.options import FunctionFormat, NumberFormat
from notion.properties.propertyobjects import (
    CheckboxPropertyObject,
    CreatedByPropertyObject,
    CreatedTimePropertyObject,
    DatabaseDescription,
    DatePropertyObject,
    EmailPropertyObject,
    FilesPropertyObject,
    FormulaPropertyObject,
    LastEditedByPropertyObject,
    LastEditedTimePropertyObject,
    MultiSelectPropertyObject,
    NumberPropertyObject,
    Option,
    PeoplePropertyObject,
    PhoneNumberPropertyObject,
    RelationPropertyObject,
    RichTextPropertyObject,
    RollupPropertyObject,
    SelectPropertyObject,
    TitlePropertyObject,
    URLPropertyObject,
)
from notion.properties.propertyvalues import Properties, TitlePropertyValue
from notion.properties.richtext import RichText
from notion.query.compound import CompoundFilter
from notion.query.propfilter import PropertyFilter
from notion.query.sort import SortFilter
from notion.query.timestamp import TimestampFilter

if TYPE_CHECKING:
    from notion.api.notionpage import Page

__all__: Sequence[str] = ["Database"]


class Database(_TokenBlockMixin):
    """
    Database objects describe the property schema of a database in Notion.
    Pages are the items (or children) in a database. The API treats database rows as pages.

    ### Title database property vs. database title
    A title database property is a type of column in a database.
    A database title defines the title of the database and is found on the database object.
    Every database requires both a database title and a title database property.

    NOTE: Adding a new column with the same name as an existing column will replace the existing column
    with the new column type. If the column of the same name is updated again, but back to the original
    column type - the previous settings (number format, formula expression, etc..) will reapply.

    ---
    ### Versioning:
    To use a previous version of the API, set the envrionment variable `NOTION_VERSION`.
    For more info see: https://developers.notion.com/reference/versioning

    ---
    :param id: (required) `database_id` of object in Notion.
    :param token: Bearer token provided when you create an integration.\
                  Set notion secret in environment variables as `NOTION_TOKEN`, or set variable here.\
                  See https://developers.notion.com/reference/authentication.

    https://developers.notion.com/reference/database
    """

    def __new__(
        cls,
        id: str,
        /,
        token: Optional[str] = None,
    ) -> Database:
        # notion api will not throw an error if the uuid isn't a database until you make a call.
        # this is to throw an error right away if trying to create a database instance
        # with a uuid that is not a database and catch the error sooner.
        target_block = Block(id, token=token)
        if target_block.type != "child_database":
            raise TypeError(f"{target_block.__repr__()} does not reference a Database.")
        return super().__new__(cls)

    def __init__(
        self,
        id: str,
        /,
        *,
        token: Optional[str] = None,
    ) -> None:
        super().__init__(id, token=token)
        self.logger = _NLOG.getChild(self.__repr__())

    @classmethod
    def create(
        cls,
        parent_instance: Page,
        database_title: str,
        name_column: Optional[str] = None,
        *,
        is_inline: Optional[bool] = False,
        description: Optional[str] = None,
        cover_url: Optional[str] = None,
        icon_url: Optional[str] = None,
    ) -> Database:
        """
        Creates a database in the specified parent page, with the specified property schema.

        ---
        :param parent_instance: (required) Parent instance for a database must be a Page.
        :param database_title: (required) Database Title.
        :param name_column: (required) Name for column containing page names. Defaults to "Name".
        :param is_inline: (optional) If true, the database will be displayed inline in the parent page.
        :param description: (optional) Description of the database.
        :param cover_url: (optional) Url of image to use as cover.
        :param icon_url: (optional) Url of image to use as icon.

        https://developers.notion.com/reference/create-a-database
        """
        payload = build_payload(
            Parent.page(parent_instance.id),
            TitlePropertyValue([RichText(database_title)]),
            Properties(TitlePropertyObject(name_column if name_column else "Name")),
        )

        new_db = cls._post(parent_instance, cls._database_endpoint(), payload=payload)

        cls_ = cls(new_db["id"])
        cls_.logger.debug(
            f"Database created in {parent_instance.__repr__()}. Url: {new_db['url']}"
        )

        if is_inline:
            cls_.is_inline = is_inline
        if description:
            cls_.description = description
        if icon_url:
            cls_.icon = icon_url
        if cover_url:
            cls_.cover = cover_url

        return cls_

    def __getitem__(self, property_name: str) -> MutableMapping[str, Any]:
        if property_name in self.property_schema:
            return cast(MutableMapping[str, Any], self.property_schema[property_name])
        raise KeyError(f"{property_name} not found in page property values.")

    def __delitem__(self, property_name_or_id: str) -> None:
        self._update({"properties": {property_name_or_id: None}})

    @cached_property
    def retrieve(self) -> MutableMapping[str, Any]:
        """
        Retrieves the database object, information that describes the structure and columns of a database.
        To fetch database rows rather than columns, use the Query a database endpoint.

        https://developers.notion.com/reference/retrieve-a-database
        """
        return self._get(self._database_endpoint(self.id))

    @property
    def property_schema(self) -> MutableMapping[str, Any]:
        return cast(MutableMapping[str, Any], self.retrieve["properties"])

    @property
    def title(self) -> str:
        """:return: (str) title of database."""
        try:
            return cast(str, self.retrieve["title"][0]["text"]["content"])
        except IndexError:
            return ""  # title is empty.

    @title.setter
    def title(self, __new_title: str) -> None:
        self._update(TitlePropertyValue([RichText(__new_title)]))

    @property
    def is_inline(self) -> bool:
        """:return: (bool) is_inline status of database.

        Has the value true if the database appears in the page as an inline block.
        Otherwise has the value false if the database appears as a child page.
        """
        return cast(bool, (self.retrieve["is_inline"]))

    @is_inline.setter
    def is_inline(self, __inline: bool) -> None:
        self._patch(
            self._database_endpoint(self.id),
            payload=default_json.dumps({"is_inline": __inline}),
        )

    @property
    def description(self) -> str:
        """
        :return: (str) description of database. Empty string if no description is set.

        description.setter:
            >>> database.description = "This is a description of the database."
        """
        try:
            description = self.retrieve["description"][0]["text"]["content"]
            return cast(str, description)
        except IndexError:
            return ""  # description is empty.

    @description.setter
    def description(self, description: str) -> None:
        self._update(DatabaseDescription([RichText(description)]))

    @property
    def icon(self) -> Union[str, None]:
        """
        :return: (str) url of icon. None if no icon is set.

        icon.setter:
            >>> database.icon = "https://www.notion.so/icons/code_gray.svg"
        """
        icon = self.retrieve["icon"]
        if icon:
            return cast(str, icon["external"]["url"])
        return None

    @icon.setter
    def icon(self, icon_url: str) -> None:
        self._update(Icon(icon_url))

    @property
    def cover(self) -> Union[str, None]:
        """
        :return: (str) url of cover. None if no cover is set.

        cover.setter:
            >>> database.cover = "https://www.notion.so/images/page-cover/webb1.jpg"
        """
        cover = self.retrieve["cover"]
        if cover:
            return cast(str, cover["external"]["url"])
        return None

    @cover.setter
    def cover(self, cover_url: str) -> None:
        self._update(Cover(cover_url))

    @property
    def url(self) -> str:
        """:return: (str) url of database"""
        return cast(str, (self.retrieve["url"]))

    @property
    def delete_self(self) -> None:
        if self.is_archived:
            return

        self._delete(self._block_endpoint(self.id))

    @property
    def restore_self(self) -> None:
        if not self.is_archived:
            return None

        self._patch(self._database_endpoint(self.id), payload=(b'{"archived": false}'))

    def _update(
        self,
        payload: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]:
        """
        Updates an existing database as specified by the parameters.

        :param payload: (required) json payload for updated properties parameters.

        https://developers.notion.com/reference/update-a-database
        """
        return self._patch(self._database_endpoint(self.id), payload=payload)

    def delete_property(self, name_or_id: str) -> None:
        """
        :param name_or_id: (required) name or id of property described in database schema

        https://developers.notion.com/reference/update-property-schema-object#removing-a-property
        """
        self._update({"properties": {name_or_id: None}})

    def rename_property(self, old_name: str, new_name: str) -> None:
        """
        https://developers.notion.com/reference/update-property-schema-object#renaming-a-property
        """
        self._update(default_json.dumps({"properties": {old_name: {"name": new_name}}}))

    def query(
        self,
        *,
        filter: Optional[Union[CompoundFilter, PropertyFilter, TimestampFilter]] = None,
        sort: Optional[SortFilter] = None,
        filter_property_values: Optional[list[str]] = None,
        page_size: Optional[int] = 100,
        start_cursor: Optional[str] = None,
    ) -> MutableMapping[str, Any]:
        """
        Gets a list of Pages contained in the database, 
        filtered/ordered to the filter conditions/sort criteria provided in request.
        Responses from paginated endpoints contain a `next_cursor` property,
        which can be used in a query payload to continue the list.

        ---
        :param filter: (optional) notion.query.compound.CompoundFilter or notion.query.propfilter.PropertyFilter
        :param sort: (optional) notion.query.sort.SortFilter
        :param page_size: (optional) The number of items from the full list desired in the response.\
                           Default: 100 page_size Maximum: 100.
        :param start_cursor: (optional) When supplied, returns a page of results starting after the cursor provided.\
                              If not supplied, this endpoint will return the first page of results.
        :param filter_property_values: (optional) Return only the selected properties.

        https://developers.notion.com/reference/post-database-query
        """
        payload: NotionObject = NotionObject()
        url = self._database_endpoint(self.id, query=True)

        if filter_property_values:
            url += "?"
            for name in filter_property_values:
                name_id = self[name].get("id")
                url += f"filter_properties={name_id}&"

        if filter:
            payload |= filter
        if sort:
            payload |= sort
        if page_size:
            payload |= {"page_size": page_size}
        if start_cursor:
            payload |= {"start_cursor": start_cursor}

        return self._post(url, payload=payload)

    def query_pages(
        self,
        *,
        filter: Optional[Union[CompoundFilter, PropertyFilter, TimestampFilter]] = None,
        sort: Optional[SortFilter] = None,
        page_size: Optional[int] = 100,
        start_cursor: Optional[str] = None,
    ) -> list[Page]:
        """
        :return: list of notion.Page objects

        :param filter: (optional) notion.query.compound.CompoundFilter or notion.query.propfilter.PropertyFilter
        :param sort: (optional) notion.query.sort.SortFilter
        :param page_size: (optional) The number of items from the full list desired in the response.\
                           Default: 100 page_size Maximum: 100.
        :param start_cursor: (optional) When supplied, returns a page of results starting after the cursor provided.\
                              If not supplied, this endpoint will return the first page of results.

        https://developers.notion.com/reference/post-database-query
        """
        query = self.query(
            filter=filter,
            sort=sort,
            page_size=page_size,
            start_cursor=start_cursor,
        )

        from notion.api.notionpage import Page

        return [Page(_object["id"]) for _object in query.get("results", [])]

    def dual_relation_column(
        self, property_name: str, /, database_id: str, synced_property_name: str
    ) -> None:
        """ Creates a `Relation` property with `Separate Directions` toggled on.

        :param property_name: (required) Name to give to property.
        :param database_id: (required) The database that the relation property refers to.\
                             The corresponding linked page values must belong to the database in order to be valid.
        :param synced_property_name: (required) The name of the corresponding property that is\
                                      updated in the related database when this property is changed.
        
        https://developers.notion.com/reference/property-object#relation
        """
        relation_property = RelationPropertyObject.dual(
            property_name, database_id, synced_property_name
        )
        self._update(Properties(relation_property))

        # NOTE: there is an issue with the current API version and `synced_property_name`,
        # Notion UI will default to `Related to {original database name} ({property name})`,
        # regardless of what name is included in the request.
        # This is a temporary fix until Notion patches this.
        try:
            Database(database_id).rename_property(
                f"Related to {self.title} ({property_name})", synced_property_name
            )
        except NotionValidationError:
            pass

    def single_relation_column(self, property_name: str, /, database_id: str) -> None:
        """ Creates a `Relation` property with `Separate Directions` toggled off.

        :param property_name: (required) Name to give to property.
        :param database_id: (required) The database id that this property will relate to.\
                             The corresponding linked page values must belong to the database in order to be valid.
        
        https://developers.notion.com/reference/property-object#relation
        """
        self._update(
            Properties(RelationPropertyObject.single(property_name, database_id))
        )

    def rollup_column(
        self,
        property_name: str,
        /,
        relation_property_name: str,
        rollup_property_name: str,
        function: Optional[
            Union[FunctionFormat, str]
        ] = FunctionFormat.show_original.value,
    ) -> None:
        """ Creates a `Rollup` property.
        A rollup database property is rendered in the Notion UI as a column with 
        values that are rollups, specific properties that are pulled from a related database.

        :param property_name: (required) Name to give to property.
        :param relation_property_name: (required) The name of the related database property that is rolled up.\
                                        i.e. if this class is databaseA, and has a column named "Related to databaseB",\
                                        then `relation_property_name` would be "Related to databaseB".
        :param rollup_property_name: (required) The name of the rollup property.\
                                      i.e if this class is databaseA, and has a column named "Related to databaseB,
                                      and you want to rollup a property in databaseB named "Number of items",\
                                      then `rollup_property_name` would be "Number of items". 
        :param function: (required) The function that computes the rollup value from the related pages.\
                          notion.properties.options.FunctionFormat or string.

        https://developers.notion.com/reference/property-object#rollup
        """
        rollup_property = RollupPropertyObject(
            property_name,
            relation_property_name,
            rollup_property_name,
            function,
        )
        self._update((Properties(rollup_property)))

    def select_column(self, property_name: str, /, options: list[Option]) -> None:
        """ Creates a `Select` property.

        If `property_name` is a select column that already exists,
        then this method will overwrite the current options - UNLESS
        if one of the options already exists and you try to change the color.
        This will raise:
        ```sh
        notion.exceptions.errors.NotionValidationError: Cannot update color of select with name: `property_name`
        ```
        You can pass an empty list to the `options` parameter to clear all choices, 
        and then re-add them with custom colors.

        :param property_name: (required) Name to give to property.
        :param options: (required) List of options to be available in the select column.\
                         `notion.properties.propertyobjects.Option`.
                         
        https://developers.notion.com/reference/property-object#select
        """
        self._update(Properties(SelectPropertyObject(property_name, options=options)))

    def multiselect_column(self, property_name: str, /, options: list[Option]) -> None:
        """ Creates a `Multi-select` property.

        If `property_name` is a multi_select column that already exists,
        then this method will overwrite the current options - UNLESS
        if one of the options already exists and you try to change the color.
        This will raise:
        ```sh
        notion.exceptions.errors.NotionValidationError: Cannot update color of select with name: `property_name`
        ```
        You can pass an empty list to the `options` parameter to clear all choices, 
        and then re-add them with custom colors.

        :param property_name: (required) Name to give to property.
        :param options: (required) List of options to be available in the select column.\
                         `notion.properties.propertyobjects.Option`.

        https://developers.notion.com/reference/property-object#multi-select
        """
        self._update(
            Properties(MultiSelectPropertyObject(property_name, options=options))
        )

    def number_column(
        self,
        property_name: str,
        /,
        format: Optional[Union[NumberFormat, str]] = NumberFormat.number.value,
    ) -> None:
        """Creates a `Number` property.

        https://developers.notion.com/reference/property-object#number
        """
        self._update(Properties(NumberPropertyObject(property_name, format)))

    def checkbox_column(self, property_name: str, /) -> None:
        """Creates a `Checkbox` property.

        https://developers.notion.com/reference/property-object#checkbox
        """
        self._update(Properties(CheckboxPropertyObject(property_name)))

    def date_column(self, property_name: str, /) -> None:
        """Creates a `Date` property.

        https://developers.notion.com/reference/property-object#date
        """
        self._update(Properties(DatePropertyObject(property_name)))

    def text_column(self, property_name: str, /) -> None:
        """Creates a `Text` property.

        https://developers.notion.com/reference/property-object#rich-text
        """
        self._update(Properties(RichTextPropertyObject(property_name)))

    def formula_column(self, property_name: str, /, expression: str) -> None:
        """ Creates a `Formula` property.

        :param expression: (required) The formula that is used to compute the values for this property.\
                            Refer to https://www.notion.so/help/formulas for more information about formula syntax.
            
        https://developers.notion.com/reference/property-object#formula
        """
        self._update(Properties(FormulaPropertyObject(property_name, expression)))

    def created_time_column(self, property_name: str, /) -> None:
        """Creates a `Created time` property.

        https://developers.notion.com/reference/property-object#created-time
        """
        self._update(Properties(CreatedTimePropertyObject(property_name)))

    def created_by_column(self, property_name: str, /) -> None:
        """Creates a `Created by` property.

        https://developers.notion.com/reference/property-object#created-by
        """
        self._update(Properties(CreatedByPropertyObject(property_name)))

    def last_edited_time_column(self, property_name: str, /) -> None:
        """Creates a `Last edited time` property.

        https://developers.notion.com/reference/property-object#last-edited-time
        """
        self._update(Properties(LastEditedTimePropertyObject(property_name)))

    def last_edited_by_column(self, property_name: str, /) -> None:
        """Creates a `Last edited by` property.

        https://developers.notion.com/reference/property-object#last-edited-by
        """
        self._update(Properties(LastEditedByPropertyObject(property_name)))

    def files_column(self, property_name: str, /) -> None:
        """Creates a `Files` property.

        https://developers.notion.com/reference/property-object#files
        """
        self._update(Properties(FilesPropertyObject(property_name)))

    def email_column(self, property_name: str, /) -> None:
        """Creates an `Email` property.

        https://developers.notion.com/reference/property-object#email
        """
        self._update(Properties(EmailPropertyObject(property_name)))

    def url_column(self, property_name: str, /) -> None:
        """Creates a `URL` property.

        https://developers.notion.com/reference/property-object#url
        """
        self._update(Properties(URLPropertyObject(property_name)))

    def phone_number_column(self, property_name: str, /) -> None:
        """Creates a `Phone` property.

        https://developers.notion.com/reference/property-object#phone-number
        """
        self._update(Properties(PhoneNumberPropertyObject(property_name)))

    def person_column(self, property_name: str, /) -> None:
        """Creates a `Person` property.

        https://developers.notion.com/reference/property-object#people
        """
        self._update(Properties(PeoplePropertyObject(property_name)))
