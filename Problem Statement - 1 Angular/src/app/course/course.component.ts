import { Component } from '@angular/core';
@Component({
   selector: 'bar-chart',
   templateUrl: './course.component.html',
   styleUrls: ['./course.component.css']
})
export class CourseComponent {
   title = 'Population (in millions)';
   type = 'BarChart';
   data = [
      ["2012", 900],
      ["2013", 1000],
      ["2014", 1170],
      ["2015", 1250],
      ["2016", 1530]
   ];
   columnNames = ['Year', 'Asia'];
   options = { };
   width = 550;
   height = 400;
}