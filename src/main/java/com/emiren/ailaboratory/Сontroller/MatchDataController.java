//package com.emiren.ailaboratory.Сontroller;
//
//import com.emiren.ailaboratory.Dto.MatchDataDto;
//import com.emiren.ailaboratory.Model.MatchData;
//import com.emiren.ailaboratory.Service.MatchDataService;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.stereotype.Controller;
//import org.springframework.ui.Model;
//import org.springframework.validation.BindingResult;
//import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.ModelAttribute;
//import org.springframework.web.bind.annotation.PathVariable;
//import org.springframework.web.bind.annotation.PostMapping;
//
//@Controller
//public class MatchDataController {
//    private MatchDataService matchDataService;
//
//    @Autowired
//    MatchDataController(MatchDataService matchDataService){
//        this.matchDataService = matchDataService;
//    }
//
//    @GetMapping("/data/new")
//    public String createEventForm(Model model){
//        MatchData data = new MatchData();
//        model.addAttribute("aiData",  data);
//        return "data-create.html";
//    }
//
//    @PostMapping("/events/{dataId}")
//    public String createData(@PathVariable("dataId") Long dataId, @ModelAttribute("matchData") MatchDataDto matchDataDto,
//                             BindingResult result,
//                             Model model) {
//        if(result.hasErrors()) {
//            model.addAttribute("matchData", matchDataDto);
//            return "data-create.html";
//        }
//        matchDataService.createData(dataId, matchDataDto);
//        return "redirect:/data/{dataId}";
//    }
//}
