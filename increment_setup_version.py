import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--level", type=int, help="Version level to increment", required=True)
args = vars(ap.parse_args())
version_level = args["level"]

if version_level not in [0, 1, 2]:  # Large, medium, small version number
    raise ValueError("The version level can only be 0, 1 or 2")

with open('setup.py') as f:
    # Read the current text
    line = f.read()
    line_processing = line.split('version="')[1]
    text_previous_version = line_processing.split('"')[0]
    digits_previous_version = [int(v) for v in text_previous_version.split('.')]
    
    # Create a new setup text
    digits_new_version = digits_previous_version
    digits_new_version[version_level] += 1
    text_new_version = [str(v) for v in digits_new_version]
    text_new_version = '.'.join(text_new_version)
    new_version = 'version="' + text_new_version + '"'
    text_setup_py = new_version.join([line.split('version="')[0], '"'.join(line_processing.split('"')[1:])])

    #print(text_setup_py)

with open('setup.py', 'w') as f:
    f.write(text_setup_py)
print(text_new_version)
#print("[INFO] Previous version: {}\tNew version: {}".format(text_previous_version, text_new_version))
