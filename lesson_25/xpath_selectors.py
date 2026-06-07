# HEADER
HEADER_LOGO = "//a[@class='header_logo']"
SIGN_IN_BUTTON = "//button[text()='Sign In']"
GUEST_LOGIN_LINK = "//button[text()='Guest log in']"
HOME = "//a[text()='Home']"
ABOUT = "//button[text()='About']"
CONTACTS = "//button[text()='Contacts']"


# SIGN IN MODAL
BUTTON_CLOSE = "//button[@aria-label='Close']"
EMAIL = "//input[@id='signinEmail']"
PASSWORD = "//input[@id='signinPassword']"
FORGOT_PASSWORD_LINK = "//button[text()='Forgot password']"
REGISTRATION = "//button[text()='Registration']"
LOGIN_BUTTON = "//button[text()='Login']"


# CONTACTS
FACEBOOK_LINK = "//a[contains(@href, 'facebook')]"
TELEGRAM_LINK = "//a[contains(@href, 't.me')]"
YOUTUBE_LINK = "//a[contains(@href, 'youtube')]"
INSTAGRAM_LINK = "//a[contains(@href, 'instagram')]"
LINKEDIN_LINK = "//a[contains(@href, 'linkedin')]"
ITHILLEL_LINK = "//a[text()='ithillel.ua']"
SUPPORT_LINK = "//a[text()='support@ithillel.ua']"


# GARAGE PAGE
ADD_BUTTON = "//button[text()='Add car']"
MY_PROFILE = "//button[@id='userNavDropdown']"


# SIDEBAR
GARAGE_SIDEBAR = "//a[contains(@class,'sidebar_btn') and @routerlink='garage']"
FUEL_EXPENSES_SIDEBAR = "//nav[contains(@class,'sidebar')]//a[@routerlink='expenses']"
INSTRUCTIONS_SIDEBAR = "//nav[contains(@class,'sidebar')]//a[@routerlink='instructions']"
LOG_OUT_BUTTON = "//a[contains(@class,'text-danger')]"


# ADD A CAR MODAL
ADD_CAR_BRAND = "//select[@id='addCarBrand']"
ADD_CAR_MODEL = "//select[@id='addCarModel']"
ADD_CAR_CANCEL_BUTTON = "//button[text()='Cancel']"
ADD_CAR_ADD_BUTTON = "//button[text()='Add']"

# MY PROFILE DROPDOWN
PROFILE_GARAGE = "//nav[contains(@class,'user-nav_menu')]//a[@routerlink='/panel/garage']"
PROFILE_FUEL_EXPENSES = "//nav[contains(@class,'user-nav_menu')]//a[@routerlink='/panel/expenses']"
PROFILE_INSTRUCTIONS = "//nav[contains(@class,'user-nav_menu')]//a[@routerlink='/panel/instructions']"
PROFILE_LOGOUT = "//nav[contains(@class,'user-nav_menu')]//button[text()='Logout']"