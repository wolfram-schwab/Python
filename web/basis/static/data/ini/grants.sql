GRANT ALL ON Buch TO 'root'@'192.168.178.54' IDENTIFIED BY 'geheim';
GRANT SELECT, INSERT ON Buch.* TO 'python'@'192.168.178.%' IDENTIFIED BY 'top-secret';