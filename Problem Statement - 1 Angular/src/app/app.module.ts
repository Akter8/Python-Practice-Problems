import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoursesComponent } from './courses.component';
import { CourseComponent } from './course/course.component';
import { CoursesService } from './courses.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { GoogleChartsModule } from 'angular-google-charts';
import { ChartsComponent } from './charts/charts.component';



@NgModule({
  declarations: [
    AppComponent,
    CoursesComponent,
    CourseComponent,
    ChartsComponent,
    
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    GoogleChartsModule,
    
  ],
  providers: [CoursesService,
    HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
