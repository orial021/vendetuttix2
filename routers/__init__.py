from routers.web.home_router import home_router
from routers.user.users_router import user_router
from routers.user.auth_router import auth_router
from routers.web.banner_router import banner_router
from routers.web.content_router import content_router
from routers.web.reviews_router import reviews_router
from routers.web.contact_router import contact_router
from routers.web.about_router import about_router
from routers.products.category_router import category_router
from routers.products.departament_router import departament_router
from routers.products.product_router import product_router

routers = [
    (home_router, '/home'),
    (user_router, '/user'),
    (auth_router, '/auth'),
    (banner_router, '/banner'),
    (content_router, '/content'),
    (reviews_router, '/reviews'),
    (contact_router, '/contact'),
    (about_router, '/about'),
    (category_router, '/category'),
    (departament_router, '/departament'),
    (product_router, '/product'),
    
] 
