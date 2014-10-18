wixmedia-python SDK
-------------------
Image Manipulation
===========================
Wix Media Services provides web developers a versatile infrastructure for image manipulations easily accessable through the Images RESTful API. 

For more details about Wix Media Services Images RESTful API, you are welcome to browse our documentation [here](https://github.com/wix/wixmedia-python/blob/master/images
_restfull_api.md). 

## Usage ##

### Uploading files ###

It’s easy to upload images using the Wixmedia Python Library. For example:

```python
from wixmedia import wixmedia_service

service = wixmedia_service.WixMediaService(api_key="my_key", api_secret="my_secret")

image = service.upload_file_from_path('/files/images/dog.jpg')
```

__Note__: Wix Media Services supports the followoing images file formats: JPEG, GIF and PNG.

### Rendering images ###

After uploading an image, you can easily apply any manipulation as described in [Wix Media Services images RESTful API](https://github.com/wix/wixmedia-python/blob/master/images
_restfull_api.md).
For example:

```python
from wixmedia import wixmedia_service

service = wixmedia_service.WixMediaService(api_key="my_key", api_secret="my_secret")
image   = service.upload_image_from_path('/files/images/dog.jpg')

print image.srz(width=120, height=120) \
           .adjust(brightness=60) \
           .filter("oil", blur=22) \
           .get_img_tag(alt="dog")
```

The above code snippet uploads an image to your account at Wix Media Services prints a HTML img tag that can be used to render the image when embedded in a web page:

```html
<img src="http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/srz/q_85,h_120,a_1,w_120,us_0.50_0.20_0.00/adjust/br_60/filter/oil,blur_22/dog.png" alt="dog">
```
#### API ####
All the APIs conform to a URI structure in the form of: 

```python
http(s)://endpoint.com/user-id/file-id/operation/params(p_value, comma-separated)/filename.ext
```
For example:
```python
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/srz/q_85,h_120,a_1,w_120,us_0.50_0.20_0.00/adjust/br_60/filter/oil,blur_22/dog.png
```
Using this python package eliminates the need to manually construct such urls. 

##### Image Transformation Operations #####

The follwoing image transformations are available (one per image maipulation request):
- Scaled resize with aligned crop   [srz]
- Scaled resize (without crop)   [srb]
- Canvas
- Fill
- Crop


###### srz - scaled resize with aligned crop ######

Scaled and resize with aligned crop, followed by unsharp mask. Most useful shortcut for simple image optimization, while maintaining good balance between output size and quality.

```python
srz(width, height, quality=75, alignment='center', radius=0.50, amount=0.20, threshold=0.00)
```

Parameter | value | Description
----------|-------|------------
width (mandatory)|Integer|The width constraint (pixels).
height (mandatory)|Integer|The height constraint (pixels).
quality (optional)|Integer (%)|The quality constraint if jpg. Values are between 0 and 100. ```default falue: 75```
alignment (optional)|string|The position pointing the place from which to start cropping  the picture (the cropping alignment). ``` default option: Central cropping.``` see values in the table below.
radius|the unsharp mask radius. ```default value: 0.50.```
amount|the unsharp mask amount. ```default value: 0.20.```
threshold|the unsharp mask threshold. ```default value: 0.00.```

alignment optional values:

Value | Description
------|------------
center|center of the image. 
top|central top part of the image.
top-left|top left part of the image.
top-right|top right part of the image.
bottom|central bottom part of the image. 
bottom-left|bottom left part of the image.
bottom-right|bottom right part of the image. 
left|central left part of the image. 
right|central right part of the image. 
face|focus on a face on the image..
faces|focus on all faces in the image.

**Sample Request**
```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')
image.srz(width=480, height=240, quality=75, alignment='top-left', radius=0.50, amount=1.20, threshold=0.00)
```
would generate the URL:
```
http://media.wixapps.net/goog:234234234234234/5d958389e0a2.jpg/srz/w_480,h_240,q_75,a_tl,us_0.50_1.20_0.00/dog.jpg
```
###### srb - scaled resize without crop ######

Resizes the image to fit within the width and height boundaries without cropping or scaling the image, but will not increase the size of the image if it is smaller than the output size. The resulting image will maintain the same aspect ratio of the input image.

```python
srb(width, height, quality=75, radius=0.50, amount=0.20, threshold=0.00)
```

Parameter | value | Description
----------|-------|------------
width (mandatory)|Integer|The width constraint (pixels).
height (mandatory)|Integer|The height constraint (pixels).
quality (optional)|Integer (%)|The quality constraint if jpg. Values are between 0 and 100. ```default value: 75```
radius|the unsharp mask radius. ```default value: 0.50.```
amount|the unsharp mask amount. ```default value: 0.20.```
threshold|the unsharp mask threshold. ```default value: 0.00.```

**Sample Request**
```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')
image.srb(width=480, height=240, quality=75)
```
would generate the URL:
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/srb/w_480,h_240,q_75,us_0.50_1.20_0.00/dog.jpg
```


###### Canvas ######

Resizes the image canvas, filling the width and height boundaries and crops any excess image data. The resulting image will match the width and height constraints without scaling the image.

```python
canvas(width, height, quality=75, alignment='center')
```

Parameter | value | Description
----------|-------|------------
width (mandatory)|Integer|The width constraint (pixels).
height (mandatory)|Integer|The height constraint (pixels).
quality (optional)|Integer (%)|The quality constraint if jpg. Values are between 0 and 100. ```default falue: 75```
alignment (optional)|string|The position pointing the place from which to start cropping  the picture (the cropping alignment). see optional values in the table below.```default value: center```

alignment optional values:

Value | Description
------|------------
center|Focus on the center of the image, both vertical and horizontal center.
top|Focus on the top of the image, horizontal center.
top-left|Focus on the top left side of the image.
top-right|Focus on the top right side of the image.
bottom|Focus on the bottom of the image, horizontal center.
bottom-left|Focus on the bottom left side of the image.
bottom-right|Focus on the bottom right side of the image.
left|Focus on the left side of the image, vertical center.
right|Focus on the right side of the image, vertical center.
face|Focus on a face on the image. Detects a face in the picture and centers on it. When multiple faces are detected in the picture, the focus will be on one of them.
faces|Focus on all faces in the image. Detects multiple faces and centers on them. Will do a best effort to have all the faces in the new image, depending on the size of the new canvas.

**Sample Request**
```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')
image.canvas(width=480, height=240, quality=75, alignment='faces')
```
would generate the URL:
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/canvas/w_480,h_240,q_75,a_fs/dog.jpg
```
and:
```python
image.canvas(width=480, height=240, quality=75)
```
would generate: (giving 'alignment' its default values)
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/canvas/w_480,h_240,q_75/dog.jpg
```


###### fill ######

Create an image with the exact given width and height while retaining original proportions. Use only part of the image that fills the given dimensions. Only part of the original image might be visible if the required proportions are different than the original ones.

```python
fill(width, height ,quality=75)
```

Parameter | value | Description
----------|-------|------------
width (mandatory)|Integer|The width constraint (pixels).
height (mandatory)|Integer|The height constraint (pixels).
quality (optional)|Integer (%)|The quality constraint if jpg. Values are between 0 and 100. ```default falue: 75```

**Sample Request**

```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')
image.fill(width=480, height=240, quality=75)
```
would generate the URL:
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/fill/w_480,h_240,q_75/dog.jpg
```
and:
```
image.fill(width=480, height=240)
```
would generate: (with the quality's default value)
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/fill/w_480,h_240/dog.jpg   
```
###### crop ######

Crops the image based on the supplied coordinates, starting at the x, y pixel coordinates along with the width and height parameters.

```python
crop(x, y, width, height, quality=75)
```

Parameter | Value | Description
----------|-------|------------
x (mandatory)|Integer|The x-pixel-coordinate to start cropping from. (represents the top-left corner point of the cropped area).
y (mandatory)|Integer|The y-pixel-coordinate to start cropping from. (represents the top-left corner point of the cropped area).
width (mandatory)|Integer|The width constraint (pixels).
height (mandatory)|Integer|The height constraint (pixels).
quality (optioanl)|Integer (%)|The quality constraint if jpg. Values are between 0 and 100. ```default value:75```

**Sample Request**
```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')
image.crop(x=120, y=120, width=480, hdight=240, quality=75)
```
would generate the URL:
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/5d958389e0a2.jpg/crop/x_120,y_120,w_480,h_240,q_75/dog.jpg
```
and:
```
image.crop(x=120, y=120, width=480, height=240)
```
would generate: (with the quality's default value)
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/5d958389e0a2.jpg/crop/x_120,y_120,w_480,h_240/dog.jpg
```


##### Image Adjustment Operation #####

Applies an adjustment to an image. Parameters values can be either specific or set to “auto”. An auto parameter without any values performs a general auto-enhancement.

```python
adjust(*props, **adjust_props)
```
the parameters may be one or more of the following options:

function | parameter(s) | Description
---------|--------------|------------
br (optional)|Integer (%)|brightness
con (optional)|Integer (%)|contrast
sat (optional)|Integer (%)|saturation
hue (optional)|Integer (%)|hue
vib (optional)|Integer (%)|vibrance
auto(optional)|-|auto adjust

**Sample Requests**
```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')

image.adjust(auto)  
would generate the URL: http://endpoint.com/5d958389e0a2.jpg/adjust/auto/dog.jpg

image.adjust(br(-82), con(12), hue(50), vib(32))  
would generate: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/adjust/br_-82,con_12,hue_50,vib_32/dog.jpg

image.adjust(con(60)) 
would generate: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/adjust/con_60/dog.jpg

image.adjust(br(100))  
would generate: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/adjust/br_100/dog.jpg
```
##### Image Filter Operation #####

Applies one (or more) of the following effects to an image: 
- Oil paint effect
- Negative effect
- Pixelate effect 
- Regular
- Based on facial recognition
- Blur
- Sharpen

```python
filter(*funcs, **filter_funcs)
```
Parameters value can be either specific values:

function | parameter(s) | Description
---------|--------------|------------
oil|-|Applies an oil paint effect on an image.
neg|-|Negates the colors of the image.
pix|Integer|Applies a pixelate effect to the image. The parameter value is the width of pixelation squares, (in pixels).
pix_faces|Integer|Applies a pixelate effect to faces in the image. The parameter value is the width of pixelation squares, (in pixels).
blur|Integer (%)|Applies a blur effect to the image. The parameter value indicates the blur in percents.
sharpen|Integer_Integer_Ingteger|Sharpens the image using radius, amount & threshold parameters. (see table below) ``` when no values are supplied, sharpen is auto```

sharpen optional values:
Value | Description | Valid values
------|-------------|-------------
radius|sharpening mask radius|0 to image size
amount|sharpening mask amount|0 to 100
threshold|shapening mask threshold|0 to 255


**Sample Requests**
```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')

image.filter(blur=50)
would generate the URL: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/filter/blur_50/dog.jpg

image.filter(oil, neg)
would generate: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/filter/oil,neg/dog.jpg

image.filter(neg, pixelate=108)
would generate: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/filter/neg,pix_108/dog.jpg

image.filter(sharpen(radius=100, amount=30, thershold=217))
would generate: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/filter/sharpen_100_30_217/dog.jpg

image.filter(oil, neg, pixelate=125, sharpen(radius=100, amount=30, thershold=217)??????)
would generate: http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/filter/oil,neg,pix_125,sharpen_100_30_217/dog.jpg

```


##### Image Watermark Operation #####

Enables users to apply watermark such as copyright notice in order to protect their images. 
* The system allows replacing watermark if needed.

```python
watermark(opacity=100, alignment='center', scale=0)
```

Parameter | value | Description
----------|-------|------------
opacity (optional)|Integer (%)|The Watermark opacity. values are between 0 and 100. ```op default value: 100.```
alignment (optional)|string|The watermark position. ``` a default option: center.``` for more details, see the table below.
scale (optional)|Integer (%)|Watermark horizontal scaling as percents of the requested image width. Values are between 0 and 100. ```scl efault value: 0```

alignment optional values:

Value | Description
------|------------
center|center of the image. 
top|central top part of the image.
top-left|top left part of the image.
top-right|top right part of the image.
bottom|central bottom part of the image. 
bottom-left|bottom left part of the image.
bottom-right|bottom right part of the image. 
left|central left part of the image. 
right|central right part of the image. 
face|face-recognition based alignment.

**Sample Request**
```python
image = wixmedia_image.WixMediaImage('http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/dog.png')
image.watermark(opacity=45, scale=0)
```
would generate the URL:
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/wm/op_45,scl_0/dog.jpg
```
and:
```python
image.watermark(opacity=100, alignment='top-left', scale=50)
```
would generate: (giving a its default values)
```
http://media.wixapps.net/goog:234234234234234/ae1d86b24054482f8477bfbf2d426936.png/wm/op_100,a_tl,scl_50/dog.jpg
```

**Sample Response**
```
{ "error": 0, "error_description": "success", "wm_filepath": "/goog:234234234234234/media/123456_wxm_88dfc1cb1babd66a7bc635dbb599d94d.jpg/dog.jpg" }
```