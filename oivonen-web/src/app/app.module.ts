import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RemoteComponent } from './remote/remote.component';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { NgxGamepadModule } from 'ngx-gamepad';

const config: SocketIoConfig = { url: 'http://localhost:8988', options: {} };

@NgModule({
  declarations: [
    AppComponent,
    RemoteComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SocketIoModule.forRoot(config),
    NgxGamepadModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }