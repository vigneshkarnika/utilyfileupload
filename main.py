import fastapi
import uvicorn
from typing import List, Optional
from starlette.background import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse
import os
from typing import Optional
import fastapi
from fastapi import UploadFile, File
from pathlib import Path
import uuid 
from wand.image import Image
from os import walk
app=fastapi.FastAPI()
directory="uploads/"
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="uploaditems/dist/",html = True), name="static")

def remove_file(path: str) -> None:
    os.unlink(path)

# @app.get("/")
# def index():
#     return fastapi.responses.HTMLResponse(
#         """
#         <!DOCTYPE html>
# <!-- Coding By CodingNepal - youtube.com/codingnepal -->
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <title>File Upload JavaScript with Progress Ba | CodingNepal</title>
#   <link rel="stylesheet" href="style.css">
#   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
#   <style>
#   @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
# *{
#   margin: 0;
#   padding: 0;
#   box-sizing: border-box;
#   font-family: "Poppins", sans-serif;
# }
# body{
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   min-height: 100vh;
#   background: #6990F2;
# }
# ::selection{
#   color: #fff;
#   background: #6990F2;
# }
# .wrapper{
#   width: 430px;
#   background: #fff;
#   border-radius: 5px;
#   padding: 30px;
#   box-shadow: 7px 7px 12px rgba(0,0,0,0.05);
# }
# .wrapper header{
#   color: #6990F2;
#   font-size: 27px;
#   font-weight: 600;
#   text-align: center;
# }
# .wrapper form{
#   height: 167px;
#   display: flex;
#   cursor: pointer;
#   margin: 30px 0;
#   align-items: center;
#   justify-content: center;
#   flex-direction: column;
#   border-radius: 5px;
#   border: 2px dashed #6990F2;
# }
# form :where(i, p){
#   color: #6990F2;
# }
# form i{
#   font-size: 50px;
# }
# form p{
#   margin-top: 15px;
#   font-size: 16px;
# }
# section .row{
#   margin-bottom: 10px;
#   background: #E9F0FF;
#   list-style: none;
#   padding: 15px 20px;
#   border-radius: 5px;
#   display: flex;
#   align-items: center;
#   justify-content: space-between;
# }
# section .row i{
#   color: #6990F2;
#   font-size: 30px;
# }
# section .details span{
#   font-size: 14px;
# }
# .progress-area .row .content{
#   width: 100%;
#   margin-left: 15px;
# }
# .progress-area .details{
#   display: flex;
#   align-items: center;
#   margin-bottom: 7px;
#   justify-content: space-between;
# }
# .progress-area .content .progress-bar{
#   height: 6px;
#   width: 100%;
#   margin-bottom: 4px;
#   background: #fff;
#   border-radius: 30px;
# }
# .content .progress-bar .progress{
#   height: 100%;
#   width: 0%;
#   background: #6990F2;
#   border-radius: inherit;
# }
# .uploaded-area{
#   max-height: 232px;
#   overflow-y: scroll;
# }
# .uploaded-area.onprogress{
#   max-height: 150px;
# }
# .uploaded-area::-webkit-scrollbar{
#   width: 0px;
# }
# .uploaded-area .row .content{
#   display: flex;
#   align-items: center;
# }
# .uploaded-area .row .details{
#   display: flex;
#   margin-left: 15px;
#   flex-direction: column;
# }
# .uploaded-area .row .details .size{
#   color: #404040;
#   font-size: 11px;
# }
# .uploaded-area i.fa-check{
#   font-size: 16px;
# }
# h4{
#     text-align:center;
# }
#   </style>


# </head>
# <body>
#   <div class="wrapper">
#     <header>JPEG Converter Utitly</header>
#     <h4>Supports .tiff,.png,.eps,.ai and .svg</h4>
#     <form action="#">
#       <input class="file-input" type="file" name="file" hidden multiple>
#       <i class="fas fa-cloud-upload-alt"></i>
#       <p>Browse File to Upload</p>
#     </form>
#     <section class="progress-area"></section>
#     <section class="uploaded-area"></section>
#   </div>
#   <script>
#   const form = document.querySelector("form"),
# fileInput = document.querySelector(".file-input"),
# progressArea = document.querySelector(".progress-area"),
# uploadedArea = document.querySelector(".uploaded-area");
# form.addEventListener("click", () =>{
#   fileInput.click();
# });
# fileInput.onchange = ({target})=>{
#   let files = target.files;
#   for(var i = 1; i <files.length; i++) {
#     var file=files[i]
#   if(file){
#     let fileName = file.name;
#     if(fileName.length >= 12){
#       let splitName = fileName.split('.');
#       fileName = splitName[0].substring(0, 13) + "... ." + splitName[1];
#     }
#     uploadFile(fileName);
#   }
# }
# }
# function uploadFile(name){
#   console.log("uploading",name)
#   let xhr = new XMLHttpRequest();
#   xhr.open("POST", "/upload");
#   xhr.responseType = 'blob';
#   xhr.upload.addEventListener("progress", ({loaded, total}) =>{
#     let fileLoaded = Math.floor((loaded / total) * 100);
#     let fileTotal = Math.floor(total / 1000);
#     let fileSize;
#     (fileTotal < 1024) ? fileSize = fileTotal + " KB" : fileSize = (loaded / (1024*1024)).toFixed(2) + " MB";
#     let progressHTML = `<li class="row">
#                           <i class="fas fa-file-alt"></i>
#                           <div class="content">
#                             <div class="details">
#                               <span class="name">${name} • Uploading</span>
#                               <span class="percent">${fileLoaded}%</span>
#                             </div>
#                             <div class="progress-bar">
#                               <div class="progress" style="width: ${fileLoaded}%"></div>
#                             </div>
#                           </div>
#                         </li>`;
#     uploadedArea.classList.add("onprogress");
#     progressArea.innerHTML = progressHTML;
#     if(loaded == total){
#       progressArea.innerHTML = "";
#       let uploadedHTML = `<li class="row">
#                             <div class="content upload">
#                               <i class="fas fa-file-alt"></i>
#                               <div class="details">
#                                 <span class="name">${name} • Uploaded</span>
#                                 <span class="size">${fileSize}</span>
#                               </div>
#                             </div>
#                             <i class="fas fa-check"></i>
#                           </li>`;
#       uploadedArea.classList.remove("onprogress");
#       uploadedArea.insertAdjacentHTML("afterbegin", uploadedHTML);
#     }
#   });
#   let data = new FormData(form);
#   xhr.onload = function(e) {
#   if (this.status == 200) {
#       var milliseconds = new Date().getTime();
#       // Create a new Blob object using the 
#       //response data of the onload object
#       var blob = new Blob([this.response], {type: 'image/jpg'});
#       //Create a link element, hide it, direct 
#       //it towards the blob, and then 'click' it programatically
#       let a = document.createElement("a");
#       a.style = "display: none";
#       document.body.appendChild(a);
#       //Create a DOMString representing the blob 
#       //and point the link element towards it
#       let url = window.URL.createObjectURL(blob);
#       a.href = url;
#       a.download = milliseconds+'.jpg';
#       //programatically click the link to trigger the download
#       a.click();
#       //release the reference to the file by revoking the Object URL
#       window.URL.revokeObjectURL(url);
#   }else{
#       //deal with your error state here
#   }
# };
#   xhr.send(data);
  
# }

#   </script>
# </body>
# </html>
#         """
#     )

@app.post("/utility/upload")
async def upload_file(file: UploadFile = File(...),name:Optional[str]=None,bg_tasks: BackgroundTasks=None):
    extension = Path(file.filename).suffix
    file_name = Path(file.filename).name
    if name is not None:
        file_name=name
    else:
        file_name=str(uuid.uuid4())
    print(file_name,extension)
    Path(directory).mkdir(parents=True, exist_ok=True)
    with open(directory+file_name+extension, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    ny = Image(filename =directory+file_name+extension)
    ny_convert = ny.convert('jpg')
    ny_convert.save(filename =directory+file_name+".jpg")
    bg_tasks.add_task(remove_file, directory+file_name+".jpg")
    bg_tasks.add_task(remove_file, directory+file_name+extension)
    return fastapi.responses.FileResponse(path=directory+file_name+".jpg", media_type='application/octet-stream', filename=file_name+".jpg")

if __name__=='__main__':
    uvicorn.run(app,port=8002,host="127.0.0.1")