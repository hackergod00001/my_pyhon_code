import subprocess
import base64

def main():
	ip="43.204.152.119"
	port=1337
	process = subprocess.Popen(["nc", ip, str(port)], stdout=subprocess.PIPE, text=True)
	
	for line in process.stdout:
		if "what does this mean" in line:
			base64_encoded_string = line.strip().split(":")[1] #Extract the base64 string after ":"
			while True:
				decoded_bytes = base64.b64decode(base64_encoded_string)
				decoded_string = decoded_bytes.decode("utf-8")
				print("Decoded:", decoded_string)
				
				if "flag" in decoded_string:
					print("Found the Flag:", decoded_string)
					break #Exit the loop if the flag is found
				else:
					base64_encoded_string = decoded_string #use the decoded string for the next iteration
					
if __name__ == "__main__":
	main()