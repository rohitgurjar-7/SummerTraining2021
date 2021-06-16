{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8853b591",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Server Side\n",
    "#lets import the libraries\n",
    "import socket,cv2,pickle,struct"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d2ed2133",
   "metadata": {},
   "outputs": [],
   "source": [
    "#socket creation\n",
    "server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "248bdf10",
   "metadata": {},
   "outputs": [],
   "source": [
    "host_name = socket.gethostname()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c24fe228",
   "metadata": {},
   "outputs": [],
   "source": [
    "host_ip = socket.gethostbyname(host_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a1d8a5c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HOST IP: 127.0.0.1\n"
     ]
    }
   ],
   "source": [
    "print('HOST IP:',host_ip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "8723a02a",
   "metadata": {},
   "outputs": [],
   "source": [
    "port = 9999"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "52a1e1da",
   "metadata": {},
   "outputs": [],
   "source": [
    "socket_address = (host_ip,port)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0fd9dbc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "server_socket.bind(socket_address)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "54e7dec8",
   "metadata": {},
   "outputs": [],
   "source": [
    "server_socket.listen(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "d7f916bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LISTENING AT: ('127.0.0.1', 9999)\n"
     ]
    }
   ],
   "source": [
    "print(\"LISTENING AT:\",socket_address)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08e4933e",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    client_socket,addr = server_socket.accept()\n",
    "    print('GOT CONNECTION FROM:',addr)\n",
    "    if client_socket:\n",
    "        vid = cv2.VideoCapture(0)\n",
    "        while(vid.isOpened()):\n",
    "            img,frame=vid.read()\n",
    "            a = pickle.dumps(frame)\n",
    "            message = struct.pack(\"Q\",len(a))+a\n",
    "            client_socket.sendall(message)\n",
    "            cv2.imshow('TRANSMITTING VIDEO',frame)\n",
    "            key=cv2.waitKey(1) & 0xFF\n",
    "            if key == ord('q'):\n",
    "                client_socket.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
