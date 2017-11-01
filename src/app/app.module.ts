import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import {AppRoutingModule} from "./app-routing.module";
import { CourseComponent } from './course/course.component';
import { RegisterCourseComponent } from './register-course/register-course.component';
import { RegistrationConfirmedComponent } from './registration-confirmed/registration-confirmed.component';


import {
  MatButtonModule, MatMenuModule, MatCardModule, MatToolbarModule, MatIconModule,MatProgressSpinnerModule } from '@angular/material';
import {TelephoneNumberFormatValidatorDirective} from "./shared/phonenumber.directive";

import {RegisterCourseService} from "app/register-course/register-course.service";
import {HttpClientModule} from "@angular/common/http";


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    CourseComponent,
    RegisterCourseComponent,
    RegistrationConfirmedComponent,
    TelephoneNumberFormatValidatorDirective,

  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatMenuModule,
    MatCardModule,
    MatToolbarModule,
    MatIconModule,
    MatProgressSpinnerModule,
  ],
  providers: [RegisterCourseService],
  bootstrap: [AppComponent]
})
export class AppModule { }
