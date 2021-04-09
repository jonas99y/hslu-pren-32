import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RemoteControlService {

  constructor(private socket: Socket) { }

  sendDriveCommand(data: DriveInstructions) {
    console.log(data)
    this.socket.emit("drive", data);
  }

  sendSpeedCommand(speedDelta:number){
    this.socket.emit("speed", speedDelta)
  }

  sendMessage(msg: string) {
    this.socket.emit("message", msg);
  }
  getMessage() {
    return this.socket
      .fromEvent("message")
      .pipe(map((data: any) => data.msg));
  }
}

export interface DriveInstructions {
  direction: number;
  speed: number;
}