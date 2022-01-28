## Size calculator for TE CL HTTP request smuggling

I wrote this simple script to easily find Content-Length and Transfer-Encoding sizes for TE CL HTTP request smuggling.

## How to

Write your data inside a txt file without the 0 which terminates the request for TE. Then: `python 3 TE_CL_size.py -f file.txt`.

Copy paste the results inside Burp, don't forget to uncheck the "Update Content-Length" in the option of Burp Repeater, and to add the 0\r\n\r\n at the end of the request.

![](_resources/presentation.gif)

Enjoy !
