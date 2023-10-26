package com.emiren.ailaboratory.Сontroller;

//import com.emiren.ailaboratory.Dto.MatchDataDto;
//import com.emiren.ailaboratory.Service.MatchDataService;
import com.emiren.ailaboratory.Model.MatchData;
import com.google.gson.Gson;
import org.springframework.http.*;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.servlet.view.RedirectView;

@RestController
public class FlaskController {
    private String flaskUrl = "http://127.0.0.1:5000";
    private String flaskMakePrediction = "http://127.0.0.1:5000/make_prediction";
    private RestTemplate restTemplate = new RestTemplate();
    HttpHeaders headers;
    Gson gson = new Gson();

    @PostMapping("/post-data")
    public RedirectView postData(@RequestParam("home_team") String home_team, @RequestParam("away_team") String away_team) {
        try {
            String jsonData = gson.toJson(new MatchData(home_team, away_team));

            headers = new org.springframework.http.HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            HttpEntity<String> requestEntity = new HttpEntity<>(jsonData, headers);
            ResponseEntity<String> response = restTemplate.exchange(flaskMakePrediction, HttpMethod.POST, requestEntity, String.class);

            System.out.println( "Data successfully sent to Flask");
        } catch (Exception e) {
            System.out.println("Failed to send data to Flask: " + e.getMessage());
        }
        return new RedirectView("/");
    }

    @GetMapping("/prediction")
    public String getPrediction(@RequestBody Integer value , Model model){


        String result;
        switch (value){
            case -1:
                result = "Home-Lose-to-Away";
            case 0:
                result = "Draw";
            case 1:
                result = "Home-wins-to-Away";
            default:
                result = "404";
        }

        model.addAttribute("result",  result);
        return "data-detail";
    }
}
