import { Component, OnInit } from '@angular/core';
import { DriveInstructions, RemoteControlService } from '../remote-control.service';
import { GamepadService } from 'ngx-gamepad';

@Component({
  selector: 'app-remote',
  templateUrl: './remote.component.html',
  styleUrls: ['./remote.component.scss']
})
export class RemoteComponent implements OnInit {
  // address:string = 'http://localhost:8988'

  constructor(private remoteController: RemoteControlService, private gamepad: GamepadService) {
  }

  ngOnInit(): void {
    this.listenToGamepad();
  }

  public onAddressUpdateClick(address:string)
  {
    this.remoteController.setAddress(address);
  }

  private listenToGamepad() {
    this.gamepad.connect()
      .subscribe(() => {

        this.gamepad.after('button15') // right
          .subscribe(() => {
            this.remoteController.sendDriveCommand({ speed: 10, direction: 2 });

          });
        this.gamepad.after('button14') // left
        .subscribe(() => {
          this.remoteController.sendDriveCommand({ speed: 10, direction: 4 });

        });
        this.gamepad.after('button12') // forward
        .subscribe(() => {
          this.remoteController.sendDriveCommand({ speed: 10, direction: 1 });

        });
        this.gamepad.after('button13') // backward
        .subscribe(() => {
          this.remoteController.sendDriveCommand({ speed: 10, direction: 3 });

        });

        this.gamepad.after('button1') // b
        .subscribe(() => {
          this.remoteController.sendDriveCommand({ speed: 10, direction: 0 });

        });

        this.gamepad.after('button7') // R2
        .subscribe(() => {
          this.remoteController.sendDriveCommand({ speed: 10, direction: 5 });

        });

        this.gamepad.after('button6') // L2
        .subscribe(() => {
          this.remoteController.sendDriveCommand({ speed: 10, direction: 6 });

        });
        this.gamepad.after('button4') // L1
        .subscribe(() => {
          this.remoteController.sendSpeedCommand(10);

        });
        this.gamepad.after('button5') // R1
        .subscribe(() => {
          this.remoteController.sendSpeedCommand(-10);

        });


      })
  }

}
