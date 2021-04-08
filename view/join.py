from .base import Base
from .option.optionViewMixin import OptionViewMixin


class Widget(Base, OptionViewMixin):
    def run(self):
        self.optionView()
        self.show()
