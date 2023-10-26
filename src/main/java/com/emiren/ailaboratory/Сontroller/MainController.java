package com.emiren.ailaboratory.Сontroller;

import com.emiren.ailaboratory.Model.MatchData;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {
    @GetMapping("/data-create")
    public String createDataForm(Model model){
        MatchData matchData = new MatchData();
        model.addAttribute("matchData", matchData);
        return "data-create";
    }

    @GetMapping("/")
    public String home(){
        return "redirect:/data-create";
    }
}
