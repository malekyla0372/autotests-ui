from elements.base_element import BaseElement


class Text(BaseElement):
    def type_of(self) -> str:
        return 'text'