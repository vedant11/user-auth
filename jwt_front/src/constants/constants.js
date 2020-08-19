// General
export const METERED_CONNECTION = 'metered_connection';
export const LOGIN_STATUS = 'login_status';
export const ROLE = 'role';
export const AUTHOR = 'author';
export const READER = 'reader';
export const USER_ID = 'user_id';
export const PROXY_URL = 'http://localhost:5005';
export const SESSION_ID = 'session_id';
export const EMAIL = 'email';
export const READER_LANGUAGE = 'reader_language';

//Post APISs
export const FORM_HANDLER = '/v1/Phone';
export const EMAIL_HANDLER = '/v1/authors';
export const READER_HANDLER = '/v1/readers';
export const REGISTRATION_HANDLER = '/v1/users';//for new user, backend yet to define
export const SLOT_HANDLER = '/v1/';//for checking available slots, yet to be defined by the backend
export const EVENT_HANDLER = '/v1/events';


//To check event slot avaibility
export const TIME_ZONE_EVENT = 'time_zone_event';
export const EVENT_DATE = 'event_date';
export const EVENT_START_TIME = 'event_start_time';
export const EVENT_END_TIME = 'event_end_time';
export const EVENT_TITLE = 'event_title';
export const EVENT_DESCRIPTION = 'event_description';
export const EVENT_STATE = 'event_state';
export const EVENT_RESOURCE_NEEDED = 'event_resource_needed';
export const LANGUAGE_EVENT = 'language_event';

//Bookings
export const BOOKING_HANDLER = '/v1/bookings';
export const EVENT_ID = 'event_id';


//Login
export const YEAR_OF_BIRTH = 'year_of_birth';
export const USER_NAME = "user_name";
export const GENDER = "gender";

// For events data fetching
export const EVENT_GET_API = '/v1/events';
//OTP validation page
export const OTP_FORM_HANDLER = '/v1/OTPverificaton';
export const PHONE_NUMBER = 'phone_number';
export const OTP = 'otp';
export const OTP_ENTERED_BY_USER = "otp_entered_by_user";
export const OTP_LENGTH = 6;
var options_year = [];
//inputing entries for options in select html element
//For guys before 1970; We can later restrict it for 'readers' 
for (let index_limit = 1970, index = 2020; index_limit <= index; index--) {
    options_year.push({
        "text": [index],
        "value": [index],
    })
}

var options_language = [
    {
        "text": "Hindi",
        "value": 'hindi',
    },
    {
        "text": "Marathi",
        "value": 'marathi',
    },
    {
        "text": "Tamil",
        "value": 'tamil',
    }
];


export { options_year, options_language };