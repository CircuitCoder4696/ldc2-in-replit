__import__('os').popen("curl -fsS https://dlang.org/install.sh | bash -s ldc");
f= open(".replit", 'w');
f.write('''
language = "bash"
run = "/home/runner/dlang/ldc-1.27.1/bin/dub run"
'''[1:-1]);
f.close();
print("LDC is installed, feel free to edit the command in `./.replit` in the string.  ");
exit();
