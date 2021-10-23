## PJT 07

관계형 데이터 베이스 설계



#### 1. Model

- 1:N, M:N 관계 설정을 위해, ForeignKey 와 ManyToManyField 사용

- 리뷰(게시글) 와 유저  **1: N** 
- 좋아요를 누른 유저와 좋아요가 눌린 리뷰(게시글) **M : N**

```python
# 1:N, M:N field 
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete= models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                        related_name='like_review')
```

- 유저에서 리뷰를 역참조 할 때 Related Manager 이름은 user.review_set

- 유저가 좋아요가 눌린 리뷰들를 역참조할 때, Related Manager 이름도 역시 user.review_set 으로 중복되어 충돌 발생

  **=> related_name 옵션으로 Related Manager 이름을 변경**

  

- 댓글 과 리뷰  **1: N**

- 댓글 과 유저 **1: N**

```python
# 1:N, M:N field 
class Comment(models.Model):
    review = models.ForeignKey(Review, 
                               on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)
```



- follow 유저 와 유저 **N : M**

```python
class User(AbstractUser):
    followings = models.ManyToManyField('self', 
                                        symmetrical=False, 
                                        related_name='followers')
```



#### 2. Review 좋아요

```python
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
        
    return redirect('community:detail', review_pk)
```

- 현재 좋아요를 요청한 user가 해당 리뷰의 좋아요를 누른 user목록에 있는지, 없는지에 따라 좋아요, 좋아요 취소 기능 구별

