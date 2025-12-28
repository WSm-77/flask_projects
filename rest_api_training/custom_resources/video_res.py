from flask_restful import Resource, reqparse, abort, marshal_with, fields
from database.models import VideoModel
from database.database_setup import db

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer,
}

put_args_parser = reqparse.RequestParser()
put_args_parser.add_argument("name", type=str, help="Provide name of the video", required = True)
put_args_parser.add_argument("views", type=int, help="Provide number of views of the video", required = True)
put_args_parser.add_argument("likes", type=str, help="Provide number of likes on the video", required = True)

patch_args_parser = reqparse.RequestParser()
patch_args_parser.add_argument("name", type=str, help="Provide name of the video")
patch_args_parser.add_argument("views", type=int, help="Provide number of views of the video")
patch_args_parser.add_argument("likes", type=str, help="Provide number of likes on the video")

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id: int):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = f"Couldn't find video id={video_id}...")

        return result

    @marshal_with(resource_fields)
    def post(self, video_id: int):
        result = VideoModel.query.filter_by(id = video_id).first()

        if result:
            abort(409, message=f"Video of id={video_id} already exists...")

        args = put_args_parser.parse_args()
        video = VideoModel(**args, id = video_id)
        db.session.add(video)
        db.session.commit()

        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = patch_args_parser.parse_args()

        (
            db.session.query(VideoModel)
                .filter(VideoModel.id == video_id)
                .update(
                    {key : value for key, value in args.items() if value is not None}
                )
        )
        db.session.commit()

        return VideoModel.query.filter_by(id = video_id).first()

    def delete(self, video_id):
        video_to_delete = VideoModel.query.filter_by(id = video_id).first()

        if not video_to_delete:
            abort(404, message = f"Couldn't find video id={video_id}...")

        db.session.delete(video_to_delete)
        db.session.commit()

        return "", 204
