import { Injectable } from '@angular/core';
import {Observable} from "rxjs/Observable";
import {HttpClient} from "@angular/common/http";
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class RegisterCourseService {
  resourceUrl= "http://localhost:5000/enroll";

  constructor(private http: HttpClient){ }

  storeRegistrationDetails(formData:any):Observable<any>{
    return this.http.post(this.resourceUrl,formData,{ observe:'response'})
      .map((response)=>{
          console.log(response);
          return { 'message' : response.body };
      }).catch((error:any)=>{
        if(error.status < 400 || error.status ===500 ){
          return Observable.throw(new Error(error.status));
        }
      });
     }
}


