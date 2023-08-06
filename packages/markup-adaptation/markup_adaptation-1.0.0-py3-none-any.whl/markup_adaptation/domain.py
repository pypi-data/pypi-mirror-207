from typing import Optional, Any, Iterable
from .common import ContentType


class DomainLocation(object):

    @property
    def content_type(self):
        return self.content_type_

    @property
    def is_cleared(self):
        return self.is_cleared_

    def __init__(self):
        self.content_type_ = None
        self.is_cleared_= False

    def get(self) -> Any:
        return None

    def set(self, content_value: Any):
        pass

    def clear(self):
        pass


class DomainLocationIterator(object):

    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self) -> DomainLocation:
        raise StopIteration()


class DomainChangeScope(object):

    def __init__(self, asset):
        self.asset = asset

    def __enter__(self):

        self.asset.change_level_ += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.asset.change_level_ -= 1

        if self.asset.change_count_ != 0 and self.asset.change_level_ == 0:
            self.asset.change_count_ = 0
            self.asset.assemble()


class DomainMixin(object):

    def __init__(self):
        pass

    def __iter__(self) -> DomainLocationIterator:
        return DomainLocationIterator()

    def select_union(self, selectors):
        return DomainMixin()

    def iterate_elements(self, selector):
        return DomainLocationIterator()

    def iterate_attributes(self, selector):
        return DomainLocationIterator()

    def iterate_content_properties(self, selector):
        return DomainLocationIterator()

    def independent_copy(self):
        return self

class DomainQueryMixin(object):

    def __init__(self):
        pass

    def apply_to(self, domain: DomainMixin) -> Optional[DomainMixin]:
        return None


class ElementQuery(DomainQueryMixin, object):

    @property
    def selectors(self):
        return iter(self.selectors_)

    def __init__(self):
        super().__init__()
        self.selectors_ = []

    def add_selector(self, selector):
        self.selectors_.append(selector)

    def apply_to(self, domain: DomainMixin) -> Optional[DomainMixin]:
        return domain.select_union(self.selectors_)


class AttributeQuery(DomainQueryMixin, object):

    @property
    def selectors(self):
        return iter(self.selectors_)

    def __init__(self):
        super().__init__()
        self.selectors_ = []

    def add_selector(self, selector):
        self.selectors_.append(selector)

    def apply_to(self, domain: DomainMixin) -> Optional[DomainMixin]:
        return domain.select_union(self.selectors_)


class ContentPropertyQuery(DomainQueryMixin, object):

    @property
    def selectors(self):
        return iter(self.selectors_)

    @property
    def property_name(self):
        return self.property_name_

    def __init__(self, property_name):
        super().__init__()
        self.selectors_ = []
        self.property_name_ = property_name

    def add_selector(self, selector):
        self.selectors_.append(selector)

    def apply_to(self, domain: DomainMixin) -> Optional[DomainMixin]:
        return domain.select_union(self.selectors_)


class StylePropertyQuery(ContentPropertyQuery):

    def __init__(self):
        super().__init__(property_name="style")


class DomainSelectorMixin(object):

    def __init__(self):
        pass

    def iterate_domain(self, domain):
        return DomainLocationIterator()


class UnionIterator(DomainLocationIterator):

    def __init__(self, domain, selectors):
        super().__init__()
        self.domain_ = domain
        self.selectors_ = list(selectors)
        self.selector_index_ = -1
        self.domain_iterator_ = None

    def __iter__(self):
        return self

    def __next__(self) -> DomainLocation:

        while True:

            try:
                if self.domain_iterator_:
                    location = next(self.domain_iterator_)
                    return location
            except StopIteration:
                pass

            self.selector_index_ += 1

            if self.selector_index_ >= len(self.selectors_):
                raise StopIteration()

            selector = self.selectors_[self.selector_index_]
            self.domain_iterator_ = selector.iterate_domain(self.domain_)


class IntersectionIterator(DomainLocationIterator):

    def __init__(self, domain, selectors):
        super().__init__()

        self.domain_ = domain
        self.selectors_ = list(selectors)
        self.intersection_ = None
        self.intersection_iterator_ = None

    def __iter__(self):
        return self

    def __next__(self) -> DomainLocation:

        if self.intersection_iterator_ is None:

            intersection = set(self.selectors_[0].apply_to(self.domain_) if self.selectors_ else [])

            for selector in self.selectors_[1:] if len(self.selectors_) > 1 else []:

                tmp_intersection = set()

                for location in selector.iterate_domain(self.domain_):

                    if location in intersection:
                        tmp_intersection.add(location)

                intersection = tmp_intersection

            self.intersection_iterator_ = iter(intersection)

        return next(self.intersection_iterator_)


ELEMENT_CONTENT_TYPE = ContentType("element")
ATTRIBUTE_CONTENT_TYPE = ContentType("attribute")
STYLE_PROPERTY_CONTENT_TYPE = ContentType("style_property")


CONTENT_PROPERTY_CONTENT_TYPES = { "style": STYLE_PROPERTY_CONTENT_TYPE }


def get_content_property_content_type(property_name, do_create=True):

    property_name = property_name.lower()
    content_type = CONTENT_PROPERTY_CONTENT_TYPES.get(property_name, None)

    if do_create and content_type is None:
        content_type = ContentType(property_name + "_property")
        CONTENT_PROPERTY_CONTENT_TYPES[property_name] = content_type

    return content_type


class ElementSelector(DomainSelectorMixin, object):

    @property
    def text(self):
        return self.text_

    @text.setter
    def text(self, value):
        self.text_ = value

    def __init__(self):
        super().__init__()
        self.text_ = ""

    def iterate_domain(self, domain):
        return domain.iterate_elements(self)


class AttributeSelector(DomainSelectorMixin, object):

    @property
    def attribute_name(self):
        return self.attribute_name_

    @attribute_name.setter
    def attribute_name(self, value):
        self.attribute_name_ = value

    @property
    def do_create_if_missing(self):
        return self.do_create_if_missing_

    @do_create_if_missing.setter
    def do_create_if_missing(self, value):
        self.do_create_if_missing_ = value

    def __init__(self):
        super().__init__()
        self.attribute_name_ = ""
        self.do_create_if_missing_ = False

    def iterate_domain(self, domain):
        return domain.iterate_attributes(self)


class ContentPropertySelector(DomainSelectorMixin, object):

    @property
    def attribute_name(self):
        return self.attribute_name_

    @property
    def property_name(self):
        return self.property_name_

    @property_name.setter
    def property_name(self, value):
        self.property_name_ = value

    @property
    def do_create_if_missing(self):
        return self.do_create_if_missing_

    @do_create_if_missing.setter
    def do_create_if_missing(self, value):
        self.do_create_if_missing_ = value

    def __init__(self, attribute_name):
        super().__init__()
        self.attribute_name_ = attribute_name
        self.property_name_ = ""
        self.do_create_if_missing_ = False

    def iterate_domain(self, domain):
        return domain.iterate_content_properties(self)


class StylePropertySelector(ContentPropertySelector):

    def __init__(self):
        super().__init__("style")
        self.property_name_ = ""
