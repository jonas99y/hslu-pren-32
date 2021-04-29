import { Injectable } from '@angular/core';
import { io, Socket } from "socket.io-client";
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RemoteControlService {
  private socket: Socket = this.createSocket('http://localhost:8988');
  constructor() {

  }

  sendDriveCommand(data: DriveInstructions) {
    console.log(data)
    this.socket.emit("drive", data);
  }

  sendSpeedCommand(speedDelta: number) {
    this.socket.emit("speed", speedDelta)
  }

  sendMessage(msg: string) {
    this.socket.emit("message", msg);
  }

  createSocket(address:string)
  {
    return io(address, {host:"*"})
  }

  setAddress(address: string) {
    this.socket.close()
    this.socket = this.createSocket(address);
  }

}

export interface DriveInstructions {
  direction: number;
  speed: number;
}
