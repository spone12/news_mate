# Inline-keyboards for dynamic actions
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

class InlineKeyboard():

    def __init__(self):
        self.builder = InlineKeyboardBuilder() 

    def create_inline_kb(self,
                         width: int,
                         buttonNames: str,
                         buttonActions: str,
                        **kwargs: str
                        ) -> InlineKeyboardMarkup:
        
        # Initialize the builder
        kbBuilder = InlineKeyboardBuilder()
        # Initialize the list for buttons
        buttons: list[InlineKeyboardButton] = []

        if buttonNames:
            for button in buttonNames:
                buttons.append(InlineKeyboardButton(
                    text=buttonActions[button] if button in buttonActions else button,
                    callback_data=button)
                )

        if kwargs:
            for button, text in kwargs.items():
                buttons.append(InlineKeyboardButton(
                    text=text,
                    callback_data=button))

        # Unpack the list with buttons into the builder using the row method with the width parameter
        kbBuilder.row(*buttons, width = width)

        # Return an inline keyboard object
        return kbBuilder.as_markup()
    