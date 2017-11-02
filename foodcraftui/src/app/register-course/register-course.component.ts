import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Validators,FormGroup, FormControl, NgForm}from '@angular/forms';
import {RegisterCourseService} from "./register-course.service";

@Component({
  selector: 'app-register-course',
  templateUrl: './register-course.component.html',
  styleUrls: ['./register-course.component.css']
})
export class RegisterCourseComponent implements OnInit {
  public myForm: FormGroup;
  loaderFlag : boolean = false;
  submitted = false;
  showErrorFlag: boolean= false;
  phonepattern = '^(?:(?:\\+?1\\s*(?:[.-]\\s*)?)?(?:\\(\\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\\s*\\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\\s*(?:[.-]\\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\\s*(?:[.-]\\s*)?([0-9]{4})(?:\\s*(?:#|x\\.?|ext\\.?|extension)\\s*(\\d+))?$';

  constructor(private registerService : RegisterCourseService, private router: Router ) {  }

  ngOnInit() {
    this.myForm = new FormGroup({
      'firstname': new FormControl("",Validators.compose([Validators.required,Validators.minLength(3)])),
      'lastname': new FormControl("",Validators.compose([Validators.required,Validators.minLength(2)])),
      'email': new FormControl("", Validators.compose([Validators.required,Validators.pattern('[a-zA-Z0-9.-_]{1,}@[a-zA-Z.-]{2,}[.]{1}[a-zA-Z]{2,}')])),
      'phoneno': new FormControl("", Validators.compose([Validators.required,Validators.maxLength(14),Validators.pattern(this.phonepattern)])),
      'courseid': new FormControl("1",Validators.compose([Validators.required]))
    });
  }

  register (myForm) {
    this.loaderFlag = true;
    console.log('Successful registration');
    console.log(myForm.value);
    this.registerService.storeRegistrationDetails(myForm.value)
      .subscribe((response)=>{
      console.log(response);
          this.loaderFlag = false;
      if(response.message == "Success"){
        this.router.navigate(['/registration-confirmed']);
      }
      this.submitted = true;
      this.clear();
      },
        (error)=>{
          console.log(error);
        this.showErrorFlag = true;
        this.loaderFlag = false;
        setTimeout(()=>{
        this.showErrorFlag = false;
        this.clear();
        },4000)
      },()=>{
          this.loaderFlag = false;
          this.showErrorFlag = false;
      })
  }

  clear(){
    this.myForm.reset();
  }


}
