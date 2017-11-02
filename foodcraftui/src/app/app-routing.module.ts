import { NgModule } from '@angular/core';
import { RouterModule, Routes} from "@angular/router";
import {CourseComponent} from "./course/course.component";
import {RegisterCourseComponent} from "./register-course/register-course.component";
import {RegistrationConfirmedComponent} from "./registration-confirmed/registration-confirmed.component";

const appRoutes: Routes =[
  {path:'', redirectTo:'course' , pathMatch:"full" },
  { path:'course', children:[
    { path:'', component: CourseComponent},
    { path:'register-course', component: RegisterCourseComponent}
  ]},
  {path:'registration-confirmed', component: RegistrationConfirmedComponent},
  {path:'**', redirectTo:'course', pathMatch:"full" }
];

@NgModule({
  imports:[RouterModule.forRoot(appRoutes)],
  exports:[RouterModule]
})
export class AppRoutingModule {}
