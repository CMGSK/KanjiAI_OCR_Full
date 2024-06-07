class Prediction{
  
  final List<Content> content;

  Prediction({
    required this.content,
  });

  factory Prediction.fromJson(Map<String, dynamic> json) => Prediction(
    content: List<Content>.from(json['result'].map((x) => Content.fromJson(x)))
    );

  Map<String, dynamic> toJson() => {
    "result": List<dynamic>.from(content.map((e) => e.toJson()))
  };
}
    

class Content {

  final String character;
  final double certainty;

  Content({
    required this.character,
    required this.certainty
  });

  factory Content.fromJson(Map<String, dynamic> json) => Content(character: json['character'], certainty: json['confidence']);
  Map<String, dynamic> toJson() => {
    "character": character,
    "certainty": certainty
  };



}