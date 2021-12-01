from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import BaseReply

from DiaRobot.Robot.nlp import Preprocess
from DiaRobot.Robot.nlp import Status

TOKEN = 'dengzhouzhang'

@csrf_exempt
def handle_wx(request):
    # GET方式用于微信公众平台绑定验证
    if request.method == 'GET':
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echo_str = request.GET.get('echostr', '')

        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            echo_str = 'error'
        response = HttpResponse(echo_str, content_type="text/plain")
        return response

    # POST方式用于接受和返回请求
    else:
        #begin 示例
        reply = None
        msg = parse_message(request.body)

        if msg.type == 'text':
            reply = create_reply('文本消息' + msg.content, msg)

        elif msg.type == 'voice':
            reply = create_reply('语音消息', msg)

        else:
            pass

        if not reply or not isinstance(reply, BaseReply):
            reply = create_reply('暂不支持您所发送的消息类型哟~ 回复“帮助”查看使用说明。', msg)

        response = HttpResponse(reply.render(), content_type="application/xml")
        return response
        #end 示例

        #todo
        #1.调用nlp.py得到语义树
        #2.根据语义树选择对应的分支模块，导航、预约、查询、推荐
        #3.生成回答并返回

        # pre = Preprocess(msg.content)
        # pre.MsgProcess()

        # if pre.status == Status.navi:
        #     pass
        # elif pre.status == Status.que:
        #     pass
        # elif pre.status == Status.recom:
        #     pass
        # elif pre.status == Status.reser:
        #     pass
        ## 用户要求不明确，需要重新输入
        # elif pre.status == Status.unclear:
        #     pass