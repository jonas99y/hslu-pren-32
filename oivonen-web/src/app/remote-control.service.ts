import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RemoteControlService {

  constructor(private socket: Socket) { }

  sendDriveCommand(data: DriveInstructions) {
    this.socket.emit("drive", data);
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