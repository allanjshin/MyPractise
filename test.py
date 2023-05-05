import subprocess

# Run the "net localgroup" command in a Windows command prompt and capture the output
output = subprocess.check_output('net localgroup', shell=True)

# Decode the output from bytes to string
output = output.decode('utf-8')

# Split the output by newline characters to get a list of lines
lines = output.split('\n')

print (lines)

# Extract the local account names and their permissions from the lines
accounts = {}
for line in lines:
    if ' * ' in line:
        account_name = line.split(' * ')[0].strip()
        permissions = line.split(' * ')[1].strip().split(',')
        accounts[account_name] = permissions

# Print the list of local accounts and their permissions
for account, permissions in accounts.items():
    print(f"{account}: {', '.join(permissions)}")