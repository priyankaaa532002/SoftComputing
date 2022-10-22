        r_eye = np.expand_dims(r_eye,axis=0)
        predict_x = model.predict(r_eye)
        rpred = np.argmax(predict_x,axis=1)
        if(rpred[0]==1):
            lbl='Open' 
        if(rpred[0]==0):
            lbl='Closed'
        break

    for (x,y,w,h) in left_eye:
        l_eye=frame[y:y+h,x:x+w]
        count=count+1
        l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
        l_eye = cv2.resize(l_eye,(24,24))
        l_eye= l_eye/255
        l_eye=l_eye.reshape(24,24,-1)
        l_eye = np.expand_dims(l_eye,axis=0)
        predict_x = model.predict(l_eye)
        lpred = np.argmax(predict_x, axis=1)
        if(lpred[0]==1):
            lbl='Open'   
