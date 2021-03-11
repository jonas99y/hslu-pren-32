import { Component, OnInit } from '@angular/core';
import { DriveInstructions, RemoteControlService } from '../remote-control.service';
import { GamepadService } from 'ngx-gamepad';

@Component({
  selector: 'app-remote',
  templateUrl: './remote.component.html',
  styleUrls: ['./remote.component.scss']
})
export class RemoteComponent implements OnInit {


  constructor(private remoteController: RemoteControlService, private gamepad: GamepadService) {
  }

  ngOnInit(): void {
    this.listenToGamepad();
  }

  private listenToGamepad() {
    this.gamepad.connect()
      .subscribe(() => {

        this.gamepad.after('button15')
          .subscribe(() => {
            this.remoteController.sendDriveCommand({ speed: 10, direction: 0 });

          });


      })
  }

}
