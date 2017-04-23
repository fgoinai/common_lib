'''
Arthor:     FGO
Usage:      Create mail server instance
Return:     SMTP server instance which is logged in already
'''
def get_smtp_server(server_addr, server_port, id, pw):
	import smtplib
    smtp_server = smtplib.SMTP(server_addr, server_port)
    smtp_server.starttls()
    smtp_server.set_debuglevel(1)
    smtp_server.login(id, pw)
    return smtp_server

'''
Arthor:     FGO
Usage:      Create mail server instance WITHOUT login
Return:     method login include server address and port -> logged in server instance
Example:
server = get_smtp_server_without_login('1.2.3.4', 8080)
server_instance = server('root', '@bcd1234')
# OR
server = get_smtp_server_without_login('1.2.3.4', 8080)('root', '@bcd1234') # I think you should use get_smtp_server
'''
def get_smtp_server_without_login(server_addr, server_port):
	import smtplib
	smtp_server = smtplib.SMTP(server_addr, server_port)

	def login(id, pw):
		smtp_server.starttls()
		smtp_server.set_debuglevel(1)
		smtp_server.login(id, pw)
		return smtp_server
	return login


'''
Arthor:     FGO
Usage:      Generate message of email, allow email with ONE attachment
Return:     method address/addr_attach -> message string
Example:
# no attachment
msg = get_msg('Subject', 'Content')([...address lsit...])
# with attachment
msg = get_msg('Subject', 'Content', True)([...address list...], attachment)
'''
def get_msg(subject, content, hv_attachment=False):
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from email.header import Header
    msg = MIMEText(content, 'html', 'utf-8') if not hv_attachment else MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8').encode()

    # Return msg string - end of fun chain
    def address(address_list):
    	# Used to encode header
    	def header_encode(s):
        	temp = ','.join(s) if isinstance(s, tuple) else s
        	return Header(temp, 'utf-8').encode()

        # msg['From'] = header_encode(address_list[0])
        msg['From'] = address_list[0]
        msg['To'] = header_encode(address_list[1])
        msg['Cc'] = header_encode(address_list[2])
        msg['Bcc'] = header_encode(address_list[3])
        return msg.as_string()

    # Used when attachment is needed, then return the final msg string directly by invoking address()
    def addr_attach(addr, atta, filename='report.csv'):
        att = MIMEText(atta, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        msg.attach(att)
        return address(addr)

    return address if not hv_attachment else addr_attach