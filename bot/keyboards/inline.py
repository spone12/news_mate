# Inline-keyboards for dynamic actions
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

class InlineKeyboard():
    """
        Inline keyboard class
    """
    
    def __init__(self):
        self.builder = InlineKeyboardBuilder() 

    def createInlineKeyBoard(self,
                         width: int,
                         buttonActions: str,
                        **kwargs: str
                        ) -> InlineKeyboardMarkup:
        
        # Initialize the builder
        kbBuilder = InlineKeyboardBuilder()
        # Initialize the list for buttons
        buttons: list[InlineKeyboardButton] = []

        if buttonActions:
            for button in buttonActions:
                buttons.append(InlineKeyboardButton(
                    text=buttonActions[button],
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
    