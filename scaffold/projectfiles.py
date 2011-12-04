"""An extremely ghetto, but functional way of creating the necessary .py files for the project setup"""
import os
import projectfolders

def create_files(project_name, root_dir):
    """Creates all of the necessary files for a given project skeleton"""
    root_dir = projectfolders.create_path(root_dir, project_name) #Modify the root
    
    write_setup(project_name, root_dir)
    write_inits(project_name, root_dir)
    

def write_setup(project_name, root_dir):
    """Writes the default setup.py file"""
    setup_path = get_file_path(root_dir, None, "setup.py") #Get the path for setup.py
    setup_content = get_setup_text(project_name)
    
    setup_file = open(setup_path, 'w')
    setup_file.write(setup_content)
    setup_file.close()
    create_file(setup_path, " +++")

def write_inits(project_name, root_dir):
    """Creates all of the __init__.py files necessary for the project skeleton"""
    
    #Create our file paths first...
    test_init_path = get_file_path(root_dir, "tests", "__init__.py")
    project_init_path = get_file_path(root_dir, project_name, "__init__.py")
    
    #Write the test_init file first
    test_init = open(test_init_path, 'w')
    test_init.close()
    create_file(test_init_path)
    
    #Write the NAME_init second
    project_init = open(project_init_path, 'w')
    project_init.close()
    create_file(project_init_path)
    
def create_file(path, prefix = ' ++++++'):
    print "create: %s %s" % (prefix, path)
    
def get_file_path(root_dir, sub_dir, filename):
    if sub_dir == None: #In case we're writing directly to the root directory
        return os.path.normpath(os.path.join(root_dir, filename))
    
    #Otherwise, build out the appropriate path for the subdirectory
    return os.path.normpath(os.path.join(projectfolders.create_path(root_dir, sub_dir), filename))

def get_setup_text(project_name):
    """This is quite ghetto, and can probably be improved"""
    
    return """
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['%s'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
""" % project_name