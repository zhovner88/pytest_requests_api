*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
List Users Should Return 200
    Create Session    reqres    https://reqres.in
    ${response}=    GET    reqres    /api/users?page=2
    Should Be Equal As Integers    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    data
    Length Should Be Greater Than    ${response.json()['data']}    0 