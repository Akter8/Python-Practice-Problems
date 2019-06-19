import { Component, OnInit } from '@angular/core';
declare const drawChart: any;
@Component({
  selector: 'app-charts',
  templateUrl: './charts.component.html',
  styleUrls: ['./charts.component.css']
})
export class ChartsComponent{
 
    title = 'Angular Tutorial';
  
     onClick() {
       drawChart();
    }
  }