from codegen import CodeGenerator
from objects import profile, cart
from tables import profiles, carts
import database


profile_codegen = CodeGenerator(database.__select_all__("profiles", "code"))
cart_codegen = CodeGenerator(database.__select_all__("carts", "cart_ids"))


def __signup__():
    code = profile_codegen.__generate__()
    cart_id = cart_codegen.__generate__()

    user = profile.Profile(
        code,
        "luroma0511",
        "This is my description",
        "luroma0511@email.com",
        "1234567890",
        None,
        cart_id
    )

    user_cart = cart.Cart(cart_id, "", 0)

    profiles.__insert__(database, user)
    carts.__insert__(database, user_cart)