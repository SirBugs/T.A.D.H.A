```
# T.A.D.H.A
Tiktok Application Data Hashing Algorithm


 @Facebook: fb/SirBugs
      @Telegram: SirBugs
            @ICQ: SirBugs

I was Getting The App Login Request ..
Suddenly I FoundOut That The Data That's Being Sent Is Hashed ..

HEADERS:
==========
POST /passport/user/login/?residence=EG&device_id=6718758026230695429&os_version=14.1&app_id=1233&iid=6893371490471167746&app_name=musical_ly&vendor_id=DFBB022B-E5F9-44F1-B2F8-75FA0F909A8B&locale=en&ac=WIFI&sys_region=EG&js_sdk_version=1.77.0.2&ssmix=a&version_code=17.8.1&vid=DFBB022B-E5F9-44F1-B2F8-75FA0F909A8B&channel=App%20Store&op_region=EG&tma_jssdk_version=1.77.0.2&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id=6893371490471167746&idfv=DFBB022B-E5F9-44F1-B2F8-75FA0F909A8B&device_platform=iphone&device_type=iPhone8%2C2&openudid=a2c9d91b7dad4214566a44f252ca8af64a987b7f&account_region=&tz_name=Africa%2FCairo&tz_offset=7200&app_language=en&carrier_region=EG&current_region=EG&aid=1233&mcc_mnc=60202&screen_width=1242&uoo=1&content_language=&language=en&cdid=6E81B29D-0443-48CA-BBBB-6ACE2358F084&build_number=178101&app_version=17.8.1&resolution=1242%2A2208 HTTP/1.1
Host: api16-normal-c-alisg.tiktokv.com
Connection: close
Content-Length: 48
Cookie: odin_tt=2e9eac5e4130390d0b6431bc2ba172830613471bc43ec918c837519861d5f82a0541eed360a3475efb2ba940a78f64747903d6e39635d649df236d3d802c4533; install_id=6893371490471167746; ttreq=1$d35ce7e5a8c33a3d0e832ff35cb5141ca6752aff; passport_csrf_token=e0e321aa63b92d57de9d4169ae9eec87; store-idc=alisg; store-country-code=eg
Content-Type: application/x-www-form-urlencoded
X-SS-Cookie: store-country-code=eg; store-idc=alisg; passport_csrf_token=e0e321aa63b92d57de9d4169ae9eec87; install_id=6893371490471167746; ttreq=1$d35ce7e5a8c33a3d0e832ff35cb5141ca6752aff; odin_tt=2e9eac5e4130390d0b6431bc2ba172830613471bc43ec918c837519861d5f82a0541eed360a3475efb2ba940a78f64747903d6e39635d649df236d3d802c4533
tt-request-time: 1604989391580
User-Agent: TikTok 17.8.1 rv:178101 (iPhone; iOS 14.1; en_EG) Cronet
x-tt-passport-csrf-token: e0e321aa63b92d57de9d4169ae9eec87
sdk-version: 2
passport-sdk-version: 5.12.1
X-SS-STUB: B700C0B450BE72CBDB4D7AA2EC1AEE09
x-tt-store-idc: alisg
x-tt-store-region: eg
X-SS-DP: 1233
x-tt-trace-id: 00-b0d29452105d3dd2d3cd4906051f04d1-b0d29452105d3dd2-01
Accept-Encoding: gzip, deflate
X-Khronos: 1604989390
X-Gorgon: 8402c08500003294d8866d16d024020912601d3813cc61663db0
==========================================================================================================================
POST Data:
============
mix_mode=1&multi_login=1&password=7f&username=71
==========================================================================================================================
Response:
============
{"data":{"alert_text":"Incorrect account or password","captcha":"","desc_url":"","description":"Incorrect account or password","error_code":1009},"message":"error"}

==========================================================================================================================
==========================================================================================================================

Then I Got The Replces For : 

-/|\:;()[]{}<>!#$%^&*=+_.@
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789

A = 44
B = 47
C = 46
D = 41
E = 40
F = 43
J = 42
H = 4d
I = 4c
J = 4f
K = 4e
L = 49
M = 48
N = 4b
O = 4a
P = 55
Q = 54
R = 57
S = 56
T = 51
U = 50
V = 53
W = 52
X = 5d
Y = 5c
Z = 5f
a = 64
b = 67
c = 66
d = 61
e = 60
f = 63
g = 62
h = 6d
i = 6c
j = 6f
k = 6e
l = 69
m = 68
n = 6b
o = 6a
p = 75
q = 74
r = 77
s = 76
t = 71
u = 70
v = 73
w = 72
x = 7d
y = 7c
z = 7f
0 = 35
1 = 34
2 = 37
3 = 36
4 = 31
5 = 30
6 = 33
7 = 32
8 = 3d
9 = 3c
- = 28
/ = 2a
| = 79
\ = 59
: = 3f
; = 3e
( = 2d
) = 2c
[ = 5e
] = 58
{ = 7e
} = 78
< = 39
> = 3b
! = 24
# = 26
$ = 21
% = 20
^ = 5b
& = 23
* = 2f
= = 38
+ = 2e
_ = 5a
. = 2b
@ = 45

And I Made A Python Script For Encrypting / Decrypting.
For Using Encrypting use [ def ENCRYPT() ]
For Using Decrypting use [ def DECRYPT() 

Have Fun!!

```
