import face_recognition
import numpy as np
import os
import glob
from services import ssh_scp as conn

def encoding_image(dir_identites):

    face_encodings=[]
    face_names=[]

    #Comment because we have one acquisition source + if we don't have the same webcam (on multiple acq source) resolution a bug append
    #conn.scp_download('mirori_faces/*', "npy_files/")

    is_npy_file = os.path.isfile('npy_files/face_names.npy')

    if is_npy_file:
        npyFaceName = np.load('npy_files/face_names.npy')
        npyFaceEncode = np.load('npy_files/face_encodings.npy')
    for dir_identite in os.listdir(dir_identites):

        fichiers=[]
        for ext in ["*.jpg", "*.jpeg", "*.png"]:
            fichiers.extend(glob.glob(dir_identites+dir_identite+"/"+ext))
        if len(fichiers)==0:
            print("Empty Folder", dir_identite)
            continue
        for fichier in fichiers:
            filename = dir_identite.replace('_', ' ')
            #print(filename not in npyFaceName)
            if is_npy_file and filename not in npyFaceName or not is_npy_file:
                image=face_recognition.load_image_file(fichier)
                embedding=face_recognition.face_encodings(image)[0]
                face_encodings.append(embedding)
                face_names.append(filename)

    if is_npy_file and len(face_names) > 0 :
        np.save("npy_files/face_encodings", np.append(npyFaceEncode, face_encodings, axis=0))
        print('Append encoding new face')
        np.save("npy_files/face_names", np.append(npyFaceName, face_names, axis=0))
        print('Append new face', face_names, '\n')
            
    elif len(face_names) > 0 :
        np.save("npy_files/face_encodings", np.array(face_encodings))
        np.save("npy_files/face_names", np.array(face_names))
        print("face encoding !")
    conn.scp_upload('npy_files/face_encodings.npy')
    conn.scp_upload('npy_files/face_names.npy')
    print("Successfuly upload!")