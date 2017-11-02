import { Injectable } from '@angular/core';
import {Observable} from "rxjs/Observable";
import {HttpClient} from "@angular/common/http";
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class RegisterCourseService {
  resourceUrl= "http://ec2-18-216-137-158.us-east-2.compute.amazonaws.com:9099/enroll";

  constructor(private http: HttpClient){ }

  storeRegistrationDetails(formData:any):Observable<any>{
    return this.http.post(this.resourceUrl,formData,{ observe:'response'})
      .map((response)=>{
          console.log(response);
          return { 'message' : response.body }
      }).catch((error:any)=>{
        if(error.status < 400 || error.status ===500 ){
          return Observable.throw(new Error(error.status));
        }
      });

    /*return Observable.create(observer => {
      const randomTime = 1000 + (Math.random() * 2000);
      setTimeout(
        function() {
          observer.next({ test: 'test' });
          observer.complete();
        }
        , randomTime);
      });*/
  }



}


