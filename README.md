#LessCSS

LessCSS is a helper which automatically compiles LESS files to CSS whenever the LESS files are modified.

It works with Brubeck and web.py web frameworks. Although it's not tested on other frameworks such as bottle, it should work without any problems.

Sample Brubeck and web.py projects are in `examples` folder.

**Note:** You need to install `less` before using this helper.

##Installation

	$ pip install lesscss

##Usage

	from lesscss import LessCSS
	LessCSS(media_dir='media', exclude_dirs=['img', 'js'], based=True)

###Parameters

- **media_dir**: Directory where you put static/media files such as css/js/img.
- **exclude_dirs**: Directories you don't want to be searched. It'd be pointless to search for `less` files in an images directory. This parameter is expected to be a list.
- **based**: If it's set `True` then LessCSS will generate the `style-(base60).css` version as well (for example; `style-dHCFD.css`). This is useful if you set expire times of static files to a distant future since browsers will not retrieve those files unless the name is different or the cache has expired. This parameter is expected to be a boolean value.
- **compressed**: If it's set `True` then LessCSS will minimize the generated CSS files. This parameter is expected to be a boolean value.
- **compression**: Specifies the type of compression to use. Default to the normal compression, 'x'. Other option is to use the [YUI Compressor](http://developer.yahoo.com/yui/compressor/css.html), 'yui'. See "Command-line Usage" at http://lesscss.org/.
- **output_dir**: Absolute path of the folder where compiled CSS files should be put.


##TODO
- Automatically set CSS name in HTML templates.

#LICENSE
Released under BSD, see LICENSE for details.

##Else
Code is based on Steve Losh's [flask-lesscss](http://sjl.bitbucket.org/flask-lesscss/).
