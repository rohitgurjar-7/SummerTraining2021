{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5fe01a30",
   "metadata": {},
   "outputs": [],
   "source": [
    "import socket,cv2,pickle,struct"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "235f4ec7",
   "metadata": {},
   "outputs": [],
   "source": [
    "client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7a5482df",
   "metadata": {},
   "outputs": [],
   "source": [
    "hosp_ip = '192.168.1.20'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c5a6f093",
   "metadata": {},
   "outputs": [],
   "source": [
    "port = 9999"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "02c273fb",
   "metadata": {},
   "outputs": [
    {
     "ename": "TimeoutError",
     "evalue": "[Errno 60] Operation timed out",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTimeoutError\u001b[0m                              Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-5-ca15cdf3ca18>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mclient_socket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'192.168.1.20'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mport\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTimeoutError\u001b[0m: [Errno 60] Operation timed out"
     ]
    }
   ],
   "source": [
    "client_socket.connect(('192.168.1.20',port))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de47a966",
   "metadata": {},
   "outputs": [],
   "source": [
    "data=b\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5261d73",
   "metadata": {},
   "outputs": [],
   "source": [
    "payload_size = struct.calcsize(\"Q\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9626eea",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    while len(data)<payload_size:\n",
    "        packet = client_socket.recv(4*1024)\n",
    "        if not packet: break\n",
    "        data+=packet\n",
    "    packed_msg_size=data[:payload_size]\n",
    "    data=data[payload_size:]\n",
    "    msg_size=struct.unpack(\"Q\",packed_msg_size)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d325f68e",
   "metadata": {},
   "outputs": [],
   "source": [
    "while len(data)<msg_size:\n",
    "    data+=client_socket.recv(4*1024)\n",
    "frame_data = data[:msg_size]\n",
    "data = data[msg_size:]\n",
    "frame = pickle.loads(frame_data)\n",
    "cv2.imshow(\"Received\",frame)\n",
    "key = cv2.waitKey(1) & 0xFF\n",
    "if key == ord('q'):\n",
    "    break\n",
    "client_socket.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bfe1348",
   "metadata": {},
   "outputs": [],
   "source": []
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
