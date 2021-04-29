import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RemoteComponent } from './remote/remote.component';
import { NgxGamepadModule } from 'ngx-gamepad';


@NgModule({
  declarations: [
    AppComponent,
    RemoteComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgxGamepadModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
