# Size calculator for HTTP/1.1 request smuggling

I wrote this simple script to easily find the different sizes for HTTP/1.1 request smuggling.

Enjoy !

## How to: TECL

Write the data inside a txt file without the 0 which terminates the request for TE. Then: `python3 sizesmuggler.py -f file.txt -t TECL`.

Copy paste the results inside Burp, don't forget to uncheck the "Update Content-Length" in the option of Burp Repeater, and to add the 0\r\n\r\n at the end of the request.

![](_resources/TECL_presentation.gif)

## How to: CLTE

Burp automatically updates the Content-Length value for CLTE if the option is checked. If you don't use Burp or want to do it yourself, write the entire data inside a txt file. Then: `python3 sizesmuggler.py -f file.txt -t CLTE`.
